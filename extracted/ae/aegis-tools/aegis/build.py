# It's really its own thing
#
# Mainly a web interface to do a build. Command line backup/repair.

# Python Imports
import datetime
import logging
import os
import requests
import shutil
import socket
import sys
import time
import traceback

# Extern Imports
import tornado.options
from tornado.options import define, options

# Project Imports
import aegis.stdlib
import aegis.model
import aegis.config


class Build:
    def __init__(self, user=None, dbconn=None):
        self.logw = aegis.stdlib.logw
        self.user = user
        self.dbconn = dbconn


    # Create a new build
    def create(self, build_args):
        if not (build_args.get('branch') or build_args.get('revision')) or not build_args.get('env'):
            return {'error': "aegis.build.Build.create(build_args) must have 'env' and one of 'branch' or 'revision'"}
        if not build_args['revision']:
            build_args['revision'] = 'HEAD'
        self.build_id = aegis.model.Build.insert_columns(dbconn=self.dbconn, **build_args)
        self.build_row = aegis.model.Build.get_id(self.build_id, dbconn=self.dbconn)
        return self.build_row


    # Perform build and distribute to hosts. Do not use nice -n within build_exec, it adds to existing process. Set hydra niceness.
    def build_exec(self, build_row):
        try:
            self.build_row = build_row
            self.start_t = time.time()
            # Environment
            self.src_dir = aegis.config.get('src_dir')
            self.src_repo = os.path.join(self.src_dir, options.program_name)
            self.username, stderr, exit_status = aegis.stdlib.shell('whoami', cwd=self.src_dir)
            self.host = socket.gethostname()
            refspec = build_row['branch']
            if build_row['revision'] != 'HEAD':
                refspec = build_row['revision']
            # Using GIT_SSH_COMMAND to specify deploy_key     https://support.circleci.com/hc/en-us/articles/21182136871835-How-to-use-a-Specific-SSH-Key-for-Git-Clone
            git_env = None
            deploy_key_path = aegis.config.get('deploy_key_path')
            if deploy_key_path:
                git_env = {'GIT_SSH_COMMAND': "ssh -i %s" % deploy_key_path}
            # Make a local clone of the repository from origin so we don't have to clone entire repository every time
            if not os.path.exists(self.src_repo):
                if self._shell_exec("git clone --progress %s %s" % (aegis.config.get('git_repo'), options.program_name), cwd=self.src_dir, build_step='build', env=git_env):
                    return
            # Fetch all the changes to repo and set the correct branch and revision
            if self._shell_exec("git fetch --all", cwd=self.src_repo, build_step='build', env=git_env):
                return
            # Reset in case there are version changes from previous builds
            if self._shell_exec("git reset --hard", cwd=self.src_repo, build_step='build', env=git_env):
                return
            if self._shell_exec("git checkout %s" % (refspec), cwd=self.src_repo, build_step='build', env=git_env):
                return
            if self._shell_exec("git pull --commit --ff", cwd=self.src_repo, build_step='build', env=git_env):
                return
            if self.build_row['revision'] == 'HEAD':
                commit_hash, stderr, exit_status = aegis.stdlib.shell('git rev-parse HEAD', cwd=self.src_repo)
                self.build_row.set_revision(commit_hash, dbconn=self.dbconn)
            # Generate new version number before cloning the new version tag into build directory
            self._new_version()
            # How was this in use? Were these all specified previously?
            #env = {"GIT_COMMITTER_NAME": options.git_committer_name, "GIT_COMMITTER_EMAIL": options.git_committer_email,
            #       "GIT_AUTHOR_NAME": options.git_committer_name, "GIT_AUTHOR_EMAIL": options.git_committer_email}
            if self._shell_exec("git tag %s" % self.next_tag, cwd=self.src_repo, build_step='build', env=git_env):
                return
            if self._shell_exec("git push --tags", cwd=self.src_repo, build_step='build', env=git_env):
                return
            self.build_row.set_version(self.next_tag, dbconn=self.dbconn)
            # Clone a fresh build into directory named by version tag
            app_dir = os.path.join(options.deploy_dir, options.program_name)
            self.build_dir = os.path.join(app_dir, self.next_tag)
            if os.path.exists(self.build_dir):
                if self._shell_exec("rm -rf %s" % self.build_dir, cwd=app_dir, build_step='build'):
                    return
            if self._shell_exec("git clone %s %s" % (self.src_repo, self.build_dir), cwd=app_dir, build_step='build', env=git_env):
                return
            # write config files into the build directory and not version control
            version_file = os.path.join(self.build_dir, options.program_name, 'version.json')
            version_json = open(version_file, 'w')
            version_json.write('{"version": "%s"}\n' % self.next_tag)
            version_json.close()
            # Set up virtualenv
            if self._shell_exec("virtualenv --python=/usr/bin/python3 --system-site-packages virtualenv", cwd=self.build_dir, build_step='build'):
                return
            if self._shell_exec("virtualenv/bin/pip --cache-dir .cache install -e .", cwd=self.build_dir, build_step='build'):
                return
            # Set up and run npm if it's installed TODO and package.lock file exists in the root of repository
            package_lock = os.path.exists(os.path.join(self.build_dir, 'package-lock.json'))
            self.npm, stderr, exit_status = aegis.stdlib.shell('which npm', cwd=self.src_dir)
            if self.npm and package_lock:
                if self._shell_exec("npm install", cwd=self.build_dir, build_step='build'):
                    return
                # If there is a next.config.mjs then build it as a next app. Otherwise run by environment name.
                next_config = os.path.exists(os.path.join(self.build_dir, 'next.config.mjs'))
                if next_config:
                    if self._shell_exec("npm run build", cwd=self.build_dir, build_step='build'):
                        return
                else:
                    if self._shell_exec("npm run %s" % self.build_row['env'], cwd=self.build_dir, build_step='build'):
                        return

            # If options.build_vite_dirs, run through them running npm run build
            build_vite_dirs = aegis.config.get('build_vite_dirs')
            aegis.stdlib.logw(build_vite_dirs, "BUILD_VITE_DIRS")
            if build_vite_dirs:
                npm_cache_dir = os.path.join(options.deploy_dir, '.npm')
                aegis.stdlib.logw(options.deploy_dir, "OPTIONS.DEPLOY_DIR")
                aegis.stdlib.logw(npm_cache_dir, "NPM_CACHE_DIR")
                for build_vite_dir in build_vite_dirs:
                    build_vite_path = os.path.join(self.build_dir, build_vite_dir)
                    aegis.stdlib.logw(build_vite_path, "BUILD_VITE_PATH")
                    if self._shell_exec("npm install --cache %s" % npm_cache_dir, cwd=build_vite_path, build_step='build'):
                        return
                    if self._shell_exec("npm run build", cwd=build_vite_path, build_step='build'):
                        logging.warning("SUCCESSFUL BUILD... ?!?")
                        return

            # Set up and run yarn if it's installed TODO and yarn.lock file exists in the root of repository
            yarn_lock = os.path.exists(os.path.join(self.build_dir, 'yarn.lock'))
            self.yarn, stderr, exit_status = aegis.stdlib.shell('which yarn', cwd=self.src_dir)
            if self.yarn and yarn_lock:
                if self._shell_exec("yarn install", cwd=self.build_dir, build_step='build'):
                    return
                if self._shell_exec("yarn run %s" % self.build_row['env'], cwd=self.build_dir, build_step='build'):
                    return
            # If we (essentially) ran webpack, build a version file and check file size
            if (self.yarn and yarn_lock) or (self.npm and package_lock):
                build_file_version = self.next_tag
                if self.build_row['env'] in options.build_local_envs:
                    build_file_version = 'local'
                if aegis.config.get('build_output_file'):
                    build_file_name = options.build_output_file % {'version': build_file_version}
                    build_output_file = os.path.join(self.build_dir, build_file_name)
                    if os.path.exists(build_output_file):
                        build_size = os.path.getsize(build_output_file)
                        if build_size:
                            self.build_row.set_build_size(build_size)
            # Rsync the files to the servers if it's configured, using non-blocking multi-shell so the rsync run in parallel
            rsync_hosts = [rh for rh in aegis.config.get('deploy_hosts') if rh != self.host]
            cmds = []
            for rsync_host in rsync_hosts:
                cmd = "rsync -q --password-file=/etc/rsync.password -avhW %s www-data@%s::%s" % (self.build_dir, rsync_host, options.rsync_module)
                cmds.append(cmd)
            for proc in aegis.stdlib.multi_shell(cmds, cwd=self.build_dir):
                stdout, stderr = proc.communicate()
                stdout = stdout.decode('utf-8').strip()
                stderr = stderr.decode('utf-8').strip()
                cmd = ' '.join(proc.args)
                if self._shell_exec(cmd, build_step='build', cwd=self.build_dir, stdout=stdout, stderr=stderr, exit_status=proc.returncode):
                    return
        except Exception as ex:
            logging.exception(ex)
            self.build_row.set_output('build', "\n%s" % traceback.format_exc(), 1, dbconn=self.dbconn)
            return self._done_exec('build', 1)
        return self._done_exec('build', 0)


    def deploy(self, version, env, build_step='deploy'):
        # Environment Settings
        deploy_build = aegis.model.Build.get_version(version, dbconn=self.dbconn)
        deploy_build = aegis.model.Build.get_id(deploy_build['build_id'], dbconn=self.dbconn)
        app_dir = os.path.join(options.deploy_dir, options.program_name)
        build_dir = os.path.join(app_dir, deploy_build['version'])
        live_symlink = os.path.join(app_dir, env)
        if deploy_build['build_target'] == 'admin':
            live_symlink = os.path.join(app_dir, "%s-admin" % env)
        # Set self.build_row for where to record output if it's deploy, but don't overwrite in the revert case
        if build_step == 'deploy':
            self.build_row = deploy_build
        self.start_t = time.time()
        self.username, stderr, exit_status = aegis.stdlib.shell('whoami')
        self.host = socket.gethostname()
        # What to restart, considering that we don't want to restart hydra from within hydra
        import __main__
        main_is_hydra = __main__.__file__.endswith('%s.py' % options.deploy_hydra_name)
        processes, stderr, exit_status = aegis.stdlib.shell("sudo /usr/bin/supervisorctl status")
        processes = [process.split(' ')[0] for process in processes.splitlines() if process.split(':')[0].endswith('_'+env) or process.split(':')[0].endswith('_'+env+'-admin')]
        num_procs = 1 if main_is_hydra else 0
        if len(processes) == num_procs:
            aegis.stdlib.loge(processes, "No processes ending with _%s to restart." % env)
        # Set up a set of <env>_prev-# to use with try_files in nginx
        # XXX Make sure to only rotate admin if it's admin   I can't remember what this comment means.
        prev_version = self.build_row['previous_version']
        if prev_version:
            for prev_num in range(1, 6):
                link_file = os.path.join(app_dir, '%s_prev-%s' % (env, prev_num))
                link_target = os.path.join(app_dir, prev_version)
                if self._shell_exec("rm -f %s" % link_file, build_step=build_step, cwd=app_dir):
                    return
                if self._shell_exec("ln -s %s %s" % (link_target, link_file), build_step=build_step, cwd=app_dir):
                    return
                # Get previous build and its previous version
                prev_build = aegis.model.Build.get_version(prev_version, dbconn=self.dbconn)
                prev_version = prev_build['previous_version']
                if not prev_version:
                    break
        # GO LIVE
        if self._shell_exec("rm -f %s" % live_symlink, build_step=build_step, cwd=app_dir):
            return
        if self._shell_exec("ln -s %s %s" % (build_dir, live_symlink), build_step=build_step, cwd=app_dir):
            return
        # Restart processes
        for process in processes:
            # Due to subprocess.Popen automatically receiving the SIGTERM from supervisor, we can't restart hydra from within supervisor.
            # https://stackoverflow.com/questions/52763508/python-prevent-child-threads-from-being-affected-from-sigint-signal
            # Instead, allow Hydra to use its quitting flag to stop and let supervisor restart.
            proc_is_hydra = process.startswith(options.deploy_hydra_name)
            if main_is_hydra and proc_is_hydra and aegis.config.get('env') == self.build_row['env']:
                logging.warning("Skip 'supervisorctl restart hydra' from within Hydra")
                continue
            # Restart processes one-by-one from supervisorctl
            # If it's an admin deploy, don't restart the other processes. And if it's the others, don't restart admin.
            if deploy_build['build_target'] == 'admin' and not process.split(':')[0].endswith('admin'):
                aegis.stdlib.logw(process, "Skip Non-Admin Process Deploying Admin")
                continue
            if deploy_build['build_target'] == 'application' and process.split(':')[0].endswith('admin'):
                aegis.stdlib.logw(process, "Skip Admin Process Deploying Application")
                continue
            if self._shell_exec("sudo /usr/bin/supervisorctl restart %s" % (process), build_step=build_step, cwd=app_dir):
                self.logw(process, "ERROR RESTARTING PROCESS")
                return
        return self._done_exec(build_step, 0)


    def revert(self, build_row):
        self.start_t = time.time()
        self.build_row = build_row
        if not self.build_row['previous_version']:
            logging.error("There is no previous version to revert to.")
            sys.exit(1)
        # Deploy the previous version, using self.build_row as the place to record it
        return self.deploy(self.build_row['previous_version'], build_row['env'], 'revert')


    def clean(self, build_row):
        # Delete all the files from filesystem for this build
        app_dir = os.path.join(options.deploy_dir, options.program_name)
        if build_row['version']:
            build_dir = os.path.join(app_dir, build_row['version'])
            if os.path.exists(build_dir):
                shutil.rmtree(build_dir)
            # If it was deleted over a month ago and the filesystem files no longer exist, just ignore this.
            elif build_row['delete_dttm'] and build_row['delete_dttm'] < datetime.datetime.utcnow() - datetime.timedelta(days=30):
                return
            build_row.set_soft_deleted(dbconn=self.dbconn)
        elif not build_row['delete_dttm']:
            self.logw(build_row['build_id'], "SOFT DELETE DOA BUILD WITH NO VERSION")
            build_row.set_soft_deleted(dbconn=self.dbconn)
        #else:
        #    self.logw(build_row['build_id'], "IS ALL DELETED")
        #self.logw(build_row['build_id'], "DONE PROCESSING BUILD ID")


    # Shell execution with structured logging and database output handling.
    def _shell_exec(self, cmd, cwd, build_step, env=None, stdout=None, stderr=None, exit_status=None):
        exec_output = "%s@%s:%s> %s" % (self.username, self.host, cwd, cmd)
        # Main case is that we're executing. But alternate is to execute elsewhere and pass in the outputs
        if exit_status is None:
            stdout, stderr, exit_status = aegis.stdlib.shell(cmd, cwd=cwd, env=env)
        if stdout:
            exec_output += '\n%s' % stdout
        if stderr:
            exec_output += "\n%s" % stderr
        exec_output += "\n"
        if exit_status:
            logging.error(exec_output.rstrip())
        else:
            logging.info(exec_output.rstrip())
        self.build_row.set_output(build_step, exec_output, dbconn=self.dbconn)
        self.build_row = aegis.model.Build.get_id(self.build_row['build_id'], dbconn=self.dbconn)
        if exit_status:
            self._done_exec(build_step, exit_status)
        return exit_status


    # Do the final summary writes after the build step is done.
    def _done_exec(self, build_step, exit_status):
        end_t = time.time()
        exec_t = end_t - self.start_t
        self.build_row.set_build_exec_sec(exec_t, self.dbconn)
        exit_line = "\n  [ Exit %s   (%4.2f sec) ]\n" % (exit_status, exec_t)
        if exit_status:
            logging.error(exit_line.rstrip())
        else:
            logging.info(exit_line.rstrip())
        self.build_row.set_output(build_step, exit_line, exit_status, self.dbconn)
        return exit_status


    # Version numbering and version files
    def _new_version(self):
        version_name = '%s_%s' % (self.build_row['env'], self.build_row['branch'])
        if self.build_row['build_target'] == 'admin':
            version_name = '%s-admin_%s' % (self.build_row['env'], self.build_row['branch'])
        version_tags, stderr, exit_status = aegis.stdlib.shell("git tag --list '%s*'" % version_name, cwd=self.src_repo)
        if version_tags:
            for version_tag in sorted(version_tags.splitlines()):
                version_num = version_tag.rsplit('-')[-1]
                version_num = tuple([int(subversion) for subversion in version_num.split('.')])
        else:
            version_num = [0, 0, 0]
        x, y, z = version_num
        #current_tag = '%s-%s.%s.%s' % (version_name, x, y, str(z).rjust(2, '0'))  # rjust to do z versions like .03 so they sort alphanumerically
        next_version = self._incr_version(*version_num)
        x, y, z = next_version
        self.next_tag = '%s-%s.%s.%s' % (version_name, x, y, str(z).rjust(2, '0'))


    # Increment minor (z) number up to 99 and the major numbers x and y to 10
    def _incr_version(self, x, y, z):
        if z < 99:
            return x, y, z+1
        z = 0
        if y < 9:
            return x, y+1, z
        y = 0
        return x+1, y, z


    # Get the commits between two versions
    @classmethod
    def commit_diff(cls, build_row, dbconn=None):
        app_dir = os.path.join(options.deploy_dir, options.program_name)
        build_dir = os.path.join(app_dir, build_row['version'])
        live_build = aegis.model.Build.get_live_build(build_row['env'], dbconn=dbconn)
        if live_build:
            commits, stderr, exit_status = aegis.stdlib.shell('git log --oneline --decorate %s..%s' % (live_build['version'], build_row['version']), cwd=build_dir)
            commits = commits.splitlines()
            return commits
        else:
            return []


    # Set previous version and send notifications
    @classmethod
    def start_deploy(cls, build_row, user, dbconn=None):
        # Set the previous version so we know what to revert back to, and mark it deployed, if this isn't happening to revert a build
        live_build = aegis.model.Build.get_live_build(build_row['env'], dbconn=dbconn)
        if live_build:
            build_row.set_previous_version(live_build['version'], dbconn=dbconn)
            build_row = aegis.model.Build.get_id(build_row['build_id'], dbconn=dbconn)
        build_row.set_deployed(dbconn=dbconn)
        # Set notifications
        commits = cls.commit_diff(build_row, dbconn=dbconn)
        notification_body = "Release Notes by %s:  %s\n\n" % (user, build_row['deploy_message'])
        notification_body += "Release Version: %s\n\n" % build_row['version']
        notification_body += "React Size: %s\n\n" % build_row['build_size']
        notification_body += "Release Commits:\n"
        for commit in commits:
            notification_body += "%s\n" % commit
        for channel in options.build_notification_channels:
            requests.post(channel, json={"text": notification_body})


    # Set to use previous version and send notifications
    @classmethod
    def start_revert(cls, build_row, user, dbconn=None):
        notification_body = "REVERT BUILD TO: %s   USER: %s   MESSAGE: %s\n\n" % (build_row['previous_version'], user, build_row['revert_message'])
        for channel in options.build_notification_channels:
            requests.post(channel, json={"text": notification_body})
        build_row.set_reverted(dbconn=dbconn)
