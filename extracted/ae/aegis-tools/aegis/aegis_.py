#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
# Aegis is your shield to protect you on the Brave New Web

# Python Imports
import argparse
import ast
import functools
import glob
import json
import logging
import os
import pwd
import sys

# Extern Imports
import tornado.options
from tornado.options import define, options

# Project Imports
aegispath = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, aegispath)
import aegis.stdlib
import aegis.build
import aegis.config


def setup_parser():
    parser = argparse.ArgumentParser(description='Create your shield.')
    parser.add_argument('cmd', metavar='<command>', type=str, nargs=1, help='What to do: [create, install, schema, build, deploy, revert]')
    parser.add_argument('--branch', metavar='<branch>', type=str, help='git branch name')
    parser.add_argument('--revision', metavar='<revision>', type=str, help='git revision hash')
    parser.add_argument('--env', metavar='<env>', type=str, help='primary environment name')
    parser.add_argument('--build_target', metavar='<build_target>', default='application', type=str, help='build target  <application, admin>')
    parser.add_argument('--version', metavar='<version>', type=str, help='program version tag')
    parser.add_argument('--appname', metavar='<appname>', type=str, nargs=1, help='code name for application')
    parser.add_argument('--domain', metavar='<domain>', type=str, nargs=1, help='domain to create application')
    parser.add_argument('--hostname', metavar='<hostname>', type=str, help='hostname to specify configs')
    parser.add_argument('--dry_run', metavar='<dry_run>', type=str, default='True', help='make no changes')
    return parser
parser = setup_parser()
parser_args = parser.parse_args()
parser_cmd = parser_args.cmd[0]


# Import config into global scope, but it isn't needed when using aegis create
if parser_cmd != 'create':
    # Load project config via VIRTUAL_ENV and naming convention, or by calling virtualenv binary directly
    venv = os.environ.get('VIRTUAL_ENV')
    if venv:
        # Running from within a virtualenv
        repo_dir = os.path.dirname(venv)
        src_dir = os.path.join(repo_dir, os.path.split(repo_dir)[-1])
        sys.path.insert(0, src_dir)
        #print("running within virtualenv")
        import config
    elif sys.argv[0] == 'virtualenv/bin/aegis':
        # Running by calling the virtualenv binary directly
        repo_dir = os.getcwd()
        src_dir = os.path.join(repo_dir, os.path.split(repo_dir)[-1])
        sys.path.insert(0, src_dir)
        #print("running from aegis cmdline")
        import config
    elif sys.argv[0] == '/usr/local/bin/aegis':
        repo_dir = os.getcwd()
        #print("running from /usr/local/bin")
        if os.path.exists(os.path.join(repo_dir, '.git')):
            src_dir = os.path.join(repo_dir, os.path.split(repo_dir)[-1])
            sys.path.insert(0, src_dir)
            try:
                import config
            except ModuleNotFoundError as ex:
                logging.exception(ex)
                logging.error("Some aegis functions won't be smooth without config.py")
        else:
            logging.error("Can't detect your app dir. Be in the source root, next to .git dir.")
            sys.exit(1)
    else:
        print(aegis.stdlib.cstr("Running in non-standard context. Going to wing it and import config. Hope this works!", 'yellow'))
        print(aegis.stdlib.cstr("Make sure you're in the source root, next to the .git dir, and in the virtualenv.", 'yellow'))
        repo_dir = os.getcwd()
        src_dir = os.path.join(repo_dir, os.path.split(repo_dir)[-1])
        sys.path.insert(0, src_dir)
        try:
            import config
        except ModuleNotFoundError as ex:
            logging.exception(ex)
            logging.error("Some aegis functions won't be smooth without config.py")


### Note to self: aegis create will work better if the core web is web.py so we don't clobber snowballin.py
# Needs templates dir, etc
# Prompt y/n to clobber with diff
# Also need aegis install, to make system admin faster
# Should all start with the /aegis stuff
# Also the sql should all be there for hydra, reports, etc



# Create a new spinoff of aegis
def create(parser):
    args = parser.parse_args()
    if not args.appname or not args.domain:
        logging.error("aegis create requires --appname and --domain")
        sys.exit()
    app_name = args.appname[0]
    domain = args.domain[0]
    aegis.stdlib.logw("AEGIS CREATE  %s  %s" % (app_name, domain))
    aegis_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    aegis.stdlib.logw(aegis_dir, "AEGIS DIR")
    src_dir = os.path.dirname(aegis_dir)
    aegis.stdlib.logw(src_dir, "SRC DIR")
    template_vars = {'app_name': app_name, 'aegis_domain': domain}
    create_dir = os.path.join(src_dir, app_name)
    #aegis.stdlib.logw(create_dir, "CREATE DIR")
    #if os.path.exists(create_dir):
    #    logging.error("AEGIS     Sorry that directory exists already. Exiting.")
    #    sys.exit(1)

    # If the directory exists prompt the user
    # You can run aegis create again to produce a new create in your repo. Then you can look at git diff to resolve and differences.

    aegis.stdlib.logw(create_dir, "CREATE DIR")
    if not os.path.exists(create_dir):
        os.mkdir(create_dir)
    create_etc_dir = os.path.join(create_dir, 'etc')
    if not os.path.exists(create_etc_dir):
        os.mkdir(create_etc_dir)
    # Now walk tmpl/etc
    tmpl_dir = os.path.join(aegis_dir, 'aegis', 'tmpl')
    for entry in os.walk(tmpl_dir):
        basedir, subdirs, files = entry
        rebasedir = create_dir + basedir[basedir.find('aegis/tmpl')+10:]
        if rebasedir.endswith('/aegis'):
            rebasedir = rebasedir[:-6] + '/' + app_name
        if not os.path.exists(rebasedir):
            os.mkdir(rebasedir)
        for filename in files:
            filepath = os.path.join(basedir, filename)
            with open(filepath, 'r') as fd:
                # iterate a dictionary of vars and replace vars
                output = fd.read()
                for var, val in template_vars.items():
                    output = output.replace('{{%s}}' % var, val)
                rebase_filename = filename
                if filename == 'aegis.py':
                    rebase_filename = app_name + '.py'


                # Needs web.py and batch with all aegis working by default
                # config.py with defaults and pre-filled program_name (only if no config.py, but definitely don't overwrite)
                # sudoers
                # github deploy key
                # supervisor should have the build configs
                # nginx should have the build configs


                if filename == 'aegis.conf':
                    rebase_filename = app_name + '.conf'
                if filename == 'aegis_dev.conf':
                    rebase_filename = app_name + '_dev.conf'
                if filename == 'aegis_prod.conf':
                    rebase_filename = app_name + '_prod.conf'
                rebasepath = os.path.join(rebasedir, rebase_filename)
                # XXX TODO diff output between one on filesystem
                # XXX maybe prompt y/n to overwrite
                with open(rebasepath, 'w') as writefd:
                    writefd.write(output)
    print ("GREAT SUCCESS!!")
    # git create and push
    # virtualenv and setup.py
    # <appname>/<appname>.py


# Diff and apply system configs to /etc and /srv
def install(parser):
    aegis.stdlib.logw(parser, "INSTALL ARG PARSER")

# Run command and log result, specific to this function
def log_cmd(cmd, aegis_dir):
    logging.info(cmd)
    stdout, stderr, exit_status = aegis.stdlib.shell(cmd, cwd=aegis_dir)
    if stdout:
        logging.info(stdout)
    if stderr:
        logging.info(stderr)

# Prep aegis release and distribute onn pypi
def release(parser):
    args = parser.parse_args()
    aegis_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    # Increment version number in distribution files
    version = aegis.stdlib.read_version()
    x, y, z = [int(ver) for ver in version.split('.')]
    new_version = "%s.%s.%s" % aegis.stdlib.incr_version(x, y, z, z_ct=9)
    aegis.stdlib.write_version(new_version)
    logging.info("New Version: %s", new_version)
    # Commit version and tag to git
    version_files = [os.path.join(aegis_dir, 'version'), os.path.join(aegis_dir, 'version.json')]
    version_files_glob = ' '.join(version_files)
    log_cmd("git commit %s -m '%s'" % (version_files_glob, new_version), aegis_dir)
    log_cmd("git tag %s" % new_version, aegis_dir)
    log_cmd("git push", aegis_dir)
    log_cmd("git push --tags", aegis_dir)
    # Packaging and uploading to pypi
    files = glob.glob(os.path.join(aegis_dir, 'dist', '*'))
    for filename in files:
        os.remove(filename)
    logging.info("Cleaned dist dir of old builds")
    log_cmd("python3 -m build", aegis_dir)
    log_cmd("python3 -m twine upload dist/*", aegis_dir)


def schema(parser):
    # Argument Handling
    args = parser.parse_args()
    schema_args = {'hostname': args.hostname, 'dry_run': ast.literal_eval(args.dry_run), 'env': aegis.config.get('env')}
    if not schema_args.get('env') or not schema_args.get('hostname'):
        logging.error("aegis schema requires --env and --hostname")
        aegis.stdlib.loge(schema_args, "SCHEMA ARGS")
        sys.exit(1)
    # Command line options and sanity checking
    if not schema_args['hostname']:
        logging.error("Please specify hostname to apply schema to, ie dev.codebug.com")
        exit(1)
    config.initialize()
    config.apply_hostname(schema_args['hostname'])
    if aegis.database.pgsql_available:
        database = options.pg_database
    elif aegis.database.mysql_available:
        database = options.mysql_database
    logging.info("Running schema.py   Env: %s   Hostname: %s   Database: %s   Dry Run: %s",
                 schema_args['env'], schema_args['hostname'], database, schema_args['dry_run'])
    if not database:
        logging.error("Database isn't configured for this hostname")
        exit(1)
    # Prime the database and sql_diff
    try:
        dbnow = aegis.database.dbnow()
        logging.warning("Database Standard Time: %s", dbnow['now'])
        if aegis.database.pgsql_available:
            results = aegis.database.db().get("SELECT EXISTS (SELECT 1 FROM pg_tables WHERE schemaname = 'public' AND tablename = 'sql_diff')")
        elif aegis.database.mysql_available:
            results = aegis.database.db().get("SELECT * FROM information_schema.tables WHERE TABLE_SCHEMA=%s AND TABLE_NAME='sql_diff'", options.mysql_database)
            results = {'exists': bool(results)}
        if not results['exists']:
            logging.warning("Creating sql_diff table since it doesn't exist yet.")
            aegis.model.SqlDiff.create_table()
    except aegis.database.PgsqlOperationalError as ex:
        logging.error("Could not connect to database. Do you need to log into postgres and run:")
        logging.error("postgres=# CREATE USER %s WITH PASSWORD '%s';" % (options.pg_username, options.pg_password))
        logging.error("postgres=# GRANT %s TO <root>;    # where root like doadmin, awsadmin" % (options.pg_username))
        logging.error("postgres=# CREATE DATABASE %s OWNER=%s;" % (options.pg_database, options.pg_username))
        exit(1)
    except aegis.database.MysqlOperationalError as ex:
        logging.error("Could not connect to database. Do you need to log into mysql and run:")
        logging.error("mysql> CREATE DATABASE %s" % (options.mysql_database))
        logging.error("mysql> USE %s" % (options.mysql_database))
        logging.error("mysql> CREATE USER '%s'@'%s' IDENTIFIED BY '%s'" % (options.mysql_username, '%', options.mysql_password))
        logging.error("mysql> GRANT ALL PRIVILEGES ON %s.* TO '%s'@'%%'" % (options.mysql_database, options.mysql_username))
        logging.error("mysql> FLUSH PRIVILEGES")
        exit(1)

    except Exception as ex:
        logging.error("Unknown Error Occurred")
        logging.exception(ex)
        exit(1)
    def diff_sort_cmp(x, y):
        xx = int(x.split('diff')[1].split('.sql')[0])
        yy = int(y.split('diff')[1].split('.sql')[0])
        return xx - yy
    def patch_diffs(sql_dir, prefix='diff'):
        if not os.path.exists(sql_dir):
            logging.error('No patch dir found at: %s', sql_dir)
            sys.exit(1)
        patches = [g.split('/')[-1] for g in glob.glob(sql_dir + '/' + prefix + '*.sql')]
        patchnums = [patch.lstrip(prefix).rstrip('.sql') for patch in patches]
        patchnums.sort()
        diffs = ['%s%s.sql' % (prefix, patchnum) for patchnum in patchnums]
        diffs = sorted(diffs, key=functools.cmp_to_key(diff_sort_cmp))
        return diffs
    # Read sql_diffs from filesystem and perform schema migrations
    sql_dir = options.basedir
    schema_path = aegis.config.get('schema_path')
    if schema_path:
        sql_dir = os.path.join(sql_dir, schema_path)
    sql_dir = os.path.join(sql_dir, 'sql')
    diff_files = patch_diffs(sql_dir)
    # Read state from database, INSERT INTO sql_diff for unknown diffs
    sql_diff_rows = aegis.model.SqlDiff.scan()
    sql_diff_map = aegis.model.SqlDiff.map_items(sql_diff_rows, 'sql_diff_name')
    for diff_file in diff_files:
        if diff_file not in sql_diff_map:
            logging.warning("Inserting diff: %s", diff_file)
            aegis.model.SqlDiff.insert(diff_file)
    # Apply any unapplied diffs
    for patch in aegis.model.SqlDiff.scan_unapplied():
        filename = os.path.join(sql_dir, patch['sql_diff_name'])
        sql = open(filename).read().replace('%', '%%')
        try:
            if schema_args['dry_run']:
                logging.warning("[Dry Run] diff:  %s  from: %s" % (patch['sql_diff_name'], filename))
            else:
                logging.warning("Applying diff:  %s  from: %s" % (patch['sql_diff_name'], filename))
                aegis.database.db().execute(sql)
                aegis.model.SqlDiff.mark_applied(patch['sql_diff_name'])
        except Exception as ex:
            logging.exception(ex)
            logging.error('Query was: %s', sql)
            exit(1)


def build(parser):
    # Argument Handling
    args = parser.parse_args()
    build_args = {'branch': args.branch, 'revision': args.revision, 'env': aegis.config.get('env'), 'build_target': args.build_target}
    if not aegis.config.get('env') or not(build_args['branch'] or build_args['revision']):
        logging.error("aegis build requires --env and one of --branch or --revision")
        aegis.stdlib.loge(aegis.config.get('env'), "ENV")
        aegis.stdlib.loge(build_args, "BUILD ARGS")
        sys.exit(1)
    # Require sudo to build, set real and effective uid and gid, as well as HOME for www-data user
    if not os.geteuid() == 0:
        logging.error('You need root privileges, please run it with sudo.')
        sys.exit(1)
    config.initialize()
    if args.hostname:
        config.apply_hostname(args.hostname)
    pw = pwd.getpwnam('www-data')
    os.putenv('HOME', pw.pw_dir)
    os.setregid(pw.pw_gid, pw.pw_gid)
    os.setreuid(pw.pw_uid, pw.pw_uid)
    # Set up build
    logging.info("Running aegis build   Env: %s   Branch: %s   Revision: %s", aegis.config.get('env'), build_args['branch'], build_args['revision'])
    # XXX Need to pass a dbconn
    new_build = aegis.build.Build()
    build_row = new_build.create(build_args)
    if build_row.get('error'):
        logging.error(build_row['error'])
        sys.exit(1)
    # Running build itself
    exit_status = new_build.build_exec(build_row)
    build_row = aegis.model.Build.get_id(build_row['build_id'])
    if exit_status:
        logging.error("Build Failed. Version: %s" % build_row['version'])
    else:
        logging.info("Build Success. Version: %s" % build_row['version'])
        next_step = "Next step:  sudo aegis deploy --env=%s --version=%s" % (aegis.config.get('env'), build_row['version'])
        if args.hostname:
            next_step += " --hostname=%s" % args.hostname
        logging.info(next_step)
    sys.exit(exit_status)


def deploy(parser):
    # Argument Handling
    args = parser.parse_args()
    version = args.version
    env = args.env
    if not version or not env:
        aegis.stdlib.logw(version, "VERSION")
        aegis.stdlib.logw(env, "ENV")
        logging.error("aegis deploy requires --version and --env")
        sys.exit()
    # Require sudo to build, set real and effective uid and gid, as well as HOME for www-data user
    if not os.geteuid() == 0:
        logging.error('You need root privileges, please run it with sudo.')
        sys.exit(1)
    config.initialize()
    if args.hostname:
        config.apply_hostname(args.hostname)
    pw = pwd.getpwnam('www-data')
    os.putenv('HOME', pw.pw_dir)
    os.setregid(pw.pw_gid, pw.pw_gid)
    os.setreuid(pw.pw_uid, pw.pw_uid)
    # Make it so
    logging.info("Running aegis deploy   Version: %s   Env: %s", version, env)
    build = aegis.build.Build()
    message = None
    while not message:
        message = input(aegis.stdlib.cstr('Type in release notes for the deploy notification:\n', 'white'))
    # Save the user message and start the deploy/revert
    build_row = aegis.model.Build.get_version(version)
    build_row.set_message(message, 'deploy')
    build_row = aegis.model.Build.get_version(version)
    aegis.build.Build.start_deploy(build_row, os.getenv('SUDO_USER'))
    build.deploy(version, env=env)


def revert(parser):
    # Argument Handling
    args = parser.parse_args()
    env = args.env
    if not env:
        aegis.stdlib.logw(env, "ENV")
        logging.error("aegis revert requires --env")
        sys.exit()
    # Require sudo to build, set real and effective uid and gid, as well as HOME for www-data user
    if not os.geteuid() == 0:
        logging.error('You need root privileges, please run it with sudo.')
        sys.exit(1)
    pw = pwd.getpwnam('www-data')
    os.putenv('HOME', pw.pw_dir)
    os.setregid(pw.pw_gid, pw.pw_gid)
    os.setreuid(pw.pw_uid, pw.pw_uid)
    # Make it so
    logging.info("Running aegis revert   Env: %s", env)
    build = aegis.build.Build()
    message = None
    while not message:
        message = input(aegis.stdlib.cstr('Type in release notes for the deploy notification:\n', 'white'))
    # Save the user message and start the deploy/revert
    build_row = aegis.model.Build.get_live_build(env)
    build_row.set_message(message, 'revert')
    build_row = aegis.model.Build.get_id(build_row['build_id'])
    aegis.build.Build.start_revert(build_row, os.getenv('SUDO_USER'))
    build_row = aegis.model.Build.get_id(build_row['build_id'])
    build_row.set_output('revert', '')
    build.revert(build_row)


def initialize():
    # if tornado options don't exist, add them
    if not aegis.config.exists('branch'):
        define('branch', default=None, help='git branch name', type=str)
    if not aegis.config.exists('revision'):
        define('revision', default=None, help='git revision hash', type=str)
    if not aegis.config.exists('version'):
        define('version', default=None, help='git version name', type=str)
    if not aegis.config.exists('dry_run'):
        define('dry_run', default='True', help='make no changes', type=str)
    if not aegis.config.exists('appname'):
        define('appname', default=None, help='name of python app', type=str)
    if not aegis.config.exists('domain'):
        define('domain', default=None, help='top level domain to host the app', type=str)
    if not aegis.config.exists('env'):
        define("env", default=None, help='[Required or set EPIPHYTE_ENV] Environment (md, prod)', type=str)
    #aegis.stdlib.logw(aegis.config.exists('env'), "AEGIS ENV")
    tornado.options.parse_command_line(sys.argv[1:])
    #aegis.stdlib.logw(aegis.config.exists('env'), "AEGIS ENV PARSED")
    #try:
    #    config.initialize(args=sys.argv[1:])
    #except Exception as ex:
    #    logging.exception(ex)
    #    # No config, such as during aegis create shell command
    #    remaining = tornado.options.parse_command_line(sys.argv[1:])
    #    print(aegis.stdlib.cstr("Remaining arguments: %s" % remaining, 'red'))



def main():
    if parser_cmd == 'create':
        return create(parser)
    elif parser_cmd == 'install':
        return install(parser)
    elif parser_cmd == 'schema':
        return schema(parser)
    elif parser_cmd == 'build':
        return build(parser)
    elif parser_cmd == 'deploy':
        return deploy(parser)
    elif parser_cmd == 'revert':
        return revert(parser)
    elif parser_cmd == 'release':
        return release(parser)
    else:
        logging.error("NOT IMPLEMENTED... YET")
        return 127

if __name__ == "__main__":
    # Called from repository checkout, for example ./aegis/aegis_.py
    initialize()
    retval = main()
    sys.exit(retval)
elif __name__ == 'aegis.aegis_':
    # Called from entry point, likely from setup.py installation
    initialize()
    retval = main()
    sys.exit(retval)
else:
    # Not entirely sure how it was called
    initialize()
    aegis.stdlib.logw(__name__, "Called by __name__")
    sys.exit(126)
