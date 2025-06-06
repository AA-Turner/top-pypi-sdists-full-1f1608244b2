# coding: utf-8
#

from __future__ import absolute_import, print_function

import argparse
import json
import logging
import sys

import adbutils

import uiautomator2 as u2
from uiautomator2.version import __version__
from uiautomator2 import enable_pretty_logging


logger = logging.getLogger(__name__)


def cmd_init(args):
    serial = args.serial or args.serial_optional
    if serial:
        d = u2.connect(serial)
        logger.debug("install apk to %s", d.serial)
        d._setup_jar()
    else:
        for dev in adbutils.adb.iter_device():
            d = u2.connect(dev)
            logger.debug("install apk to %s", d.serial)
            d._setup_jar()
            d._setup_ime()


def cmd_purge(args):
    """remove minicap, minitouch, uiautomator ..."""
    dev = adbutils.adb.device(args.serial)
    dev.uninstall("com.github.uiautomator")
    dev.uninstall("com.github.uiautomator.test")
    dev.shell(["/data/local/tmp/atx-agent", "server", "--stop"])
    dev.shell(["rm", "/data/local/tmp/atx-agent"])
    logger.info("atx-agent stopped and removed")
    dev.shell(["rm", "/data/local/tmp/minicap"])
    dev.shell(["rm", "/data/local/tmp/minicap.so"])
    dev.shell(["rm", "/data/local/tmp/minitouch"])
    logger.info("minicap, minitouch removed")
    dev.shell(["pm", "uninstall", "com.github.uiautomator"])
    dev.shell(["pm", "uninstall", "com.github.uiautomator.test"])
    logger.info("com.github.uiautomator uninstalled, all done !!!")


def cmd_screenshot(args):
    d = u2.connect(args.serial)
    d.screenshot().save(args.filename)
    print("Save screenshot to %s" % args.filename)


def cmd_install(args):
    u = u2.connect(args.serial)
    pkg_name = u.app_install(args.url)
    print("Installed", pkg_name)


def cmd_uninstall(args):
    d = u2.connect(args.serial)
    if args.all:
        d.app_uninstall_all(verbose=True)
    else:
        for package_name in args.package_name:
            print('Uninstall "%s" ' % package_name, end="", flush=True)
            ok = d.app_uninstall(package_name)
            print("OK" if ok else "FAIL")


def cmd_start(args):
    d = u2.connect(args.serial)
    d.app_start(args.package_name)


def cmd_stop(args):
    d = u2.connect(args.serial)
    if args.all:
        d.app_stop_all()
        return

    for package_name in args.package_name:
        print('am force-stop "%s" ' % package_name)
        d.app_stop(package_name)


def cmd_current(args):
    d = u2.connect(args.serial)
    print(json.dumps(d.app_current(), indent=4), flush=True)


def cmd_doctor(args):
    """check if environment is fine"""
    d = u2.connect(args.serial)
    logger.debug("device serial: %s", d.serial)
    try:
        d.info
        logger.info("uiautomator2 is OK")
    except Exception as e:
        logger.error("error: %s", e)
        sys.exit(1)


def cmd_version(args):
    """print uiautomator2 lib version"""
    print("uiautomator2 version: %s" % __version__)


def cmd_console(args):
    import code
    import platform
    
    d = u2.connect(args.serial)
    model = d.shell("getprop ro.product.model").output.strip()
    serial = d.serial
    try:
        import IPython
        from traitlets.config import get_config

        c = get_config()
        c.InteractiveShellEmbed.colors = "neutral"
        IPython.embed(config=c, header=f"IPython is ready, uiautomator2: {__version__}, try d.info")
    except ImportError:
        _vars = globals().copy()
        _vars.update(locals())
        shell = code.InteractiveConsole(_vars)
        shell.interact(
            banner="Python: %s\nDevice: %s(%s)"
            % (platform.python_version(), model, serial)
        )


_commands = [
    dict(action=cmd_version, command="version", help="show version"),
    dict(
        action=cmd_init,
        command="init",
        help="install enssential resources to device",
        flags=[
            dict(
                args=["--addr"],
                default="127.0.0.1:7912",
                help="atx-agent listen address",
            ),
            dict(args=["--serial", "-s"], type=str, help="serial number"),
            dict(
                args=["serial_optional"],
                nargs="?",
                help="serial number, same as --serial",
            ),
        ],
    ),
    dict(
        action=cmd_screenshot,
        command="screenshot",
        help="take device screenshot",
        flags=[
            dict(
                args=["filename"],
                nargs="?",
                default="screenshot.jpg",
                type=str,
                help="output filename, jpg or png",
            )
        ],
    ),
    dict(
        action=cmd_install,
        command="install",
        help="install packages",
        flags=[
            dict(args=["url"], help="package url"),
        ],
    ),
    dict(
        action=cmd_uninstall,
        command="uninstall",
        help="uninstall packages",
        flags=[
            dict(args=["--all"], action="store_true", help="uninstall all packages"),
            dict(args=["package_name"], nargs="*", help="package name"),
        ],
    ),
    dict(
        action=cmd_start,
        command="start",
        help="start application",
        flags=[dict(args=["package_name"], type=str, nargs=None, help="package name")],
    ),
    dict(
        action=cmd_stop,
        command="stop",
        help="stop application",
        flags=[
            dict(args=["--all"], action="store_true", help="stop all"),
            dict(args=["package_name"], nargs="*", help="package name"),
        ],
    ),
    dict(action=cmd_current, command="current", help="show current application"),
    dict(action=cmd_doctor, command="doctor", help="detect connect problem"),
    dict(
        action=cmd_console, command="console", help="launch interactive python console"
    ),
    dict(
        action=cmd_purge,
        command="purge",
        help="remove minitouch, minicap, atx app etc, from device",
    ),
]


def main():
    # yapf: disable
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--debug", action="store_true",
                        help="show log")
    parser.add_argument('-s', '--serial', type=str,
                        help='device serial number')

    subparser = parser.add_subparsers(dest='subparser')

    actions = {}
    for c in _commands:
        cmd_name = c['command']
        actions[cmd_name] = c['action']
        sp = subparser.add_parser(cmd_name, help=c.get('help'),
                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        for f in c.get('flags', []):
            args = f.get('args')
            if not args:
                args = ['-'*min(2, len(n)) + n for n in f['name']]
            kwargs = f.copy()
            kwargs.pop('name', None)
            kwargs.pop('args', None)
            sp.add_argument(*args, **kwargs)

    args = parser.parse_args()
    enable_pretty_logging()

    if args.debug:
        logger.debug("args: %s", args)

    if args.subparser:
        actions[args.subparser](args)
        return

    parser.print_help()
    # yapf: enable


if __name__ == "__main__":
    main()
