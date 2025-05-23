# -----------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -----------------------------------------------------------------------------
# pylint: disable=line-too-long
import os
ENCODING = 'utf-8'

# Base on https://github.com/Azure/azure-cli/blob/dev/.github/CODEOWNERS
# Add identity after pr 21041
# Move container out of CLI_OWN_MODULES, this module cannot find an owner in service team.
# Move privatedns out of CLI_OWN_MODULES, this module cannot find an owner in service team.
CLI_OWN_MODULES = [
    'cloud',
    'databoxedge',
    'identity',
    'keyvault',
    'monitor',
    'network',
    'profile',
    'resource',
    'role',
    'storage',
    'vm',
    'azext_account',
    'azext_ad',
    'azext_automanage',
    'azext_automation',
    'azext_azure-firewall',
    'azext_blockchain',
    # 'azext_cloudservice', # azure-mgmt-compute~=20.0.0 (azure-mgmt-compute-29.0.0) install failed
    'azext_communication',
    'azext_confluent',
    # 'azext_connection-monitor-preview', # compatible with your current CLI core version 2.44.1.（2.0.81）
    'azext_costmanagement',
    'azext_custom-providers',
    'azext_databox',
    'azext_datafactory',
    'azext_dns-resolver',
    'azext_dynatrace',
    'azext_edgeorder',
    'azext_elastic',
    'azext_express-route-cross-connection',
    'azext_healthcareapis',
    'azext_hpc-cache',
    'azext_image-gallery',
    'azext_init',
    'azext_interactive',
    'azext_internet-analyzer',
    'azext_ip-group',
    'azext_keyvault-preview',
    'azext_log-analytics-solution',
    'azext_logic',
    'azext_logz',
    'azext_mobile-network',
    'azext_monitor-control-service',
    'azext_network-manager',
    'azext_next',
    'azext_peering',
    'azext_purview',
    'azext_scheduled-query',
    'azext_stack-hci',
    'azext_storage-blob-preview',
    'azext_storage-preview',
    'azext_storagesync',
    'azext_swiftlet',
    'azext_timeseriesinsights',
    'azext_virtual-network-tap',
    'azext_virtual-wan',
]

EXCLUDE_MODULES = [
    'batchai',
    'extension',
    'feedback',
    'find',
    'interactive',
    'kusto',
    'util'
]

# refer to doc: https://review.learn.microsoft.com/en-us/help/platform/metadata-taxonomies/allowed-html?branch=main
ALLOWED_HTML_TAG = [
    "a", "address", "article", "b", "blockquote", "button", "br", "br /",
    "/a", "/address", "/article", "/b", "/blockquote", "/button", "/br", "br/",
    "caption", "center", "cite", "code", "col", "colgroup",
    "/caption", "/center", "/cite", "/code", "/col", "/colgroup",
    "dd", "del", "details", "div", "dl", "dt", "em", "figcaption", "figure", "form",
    "/dd", "/del", "/details", "/div", "/dl", "/dt", "/em", "/figcaption", "/figure", "/form",
    "h1", "h2", "h3", "h4", "head", "hr",
    "/h1", "/h2", "/h3", "/h4", "/head", "/hr",
    "i", "iframe", "image", "img", "input", "ins", "kbd",
    "/i", "/iframe", "/image", "/img", "/input", "/ins", "/kbd",
    "label", "li", "nav", "nobr", "ol", "p", "pre", "rgn",
    "/label", "/li", "/nav", "/nobr", "/ol", "/p", "/pre", "/rgn",
    "s", "section", "source", "span", "strike", "strong", "sub", "summary", "sup",
    "/s", "/section", "/source", "/span", "/strike", "/strong", "/sub", "/summary", "/sup",
    "table", "tbody", "td", "tfoot", "th", "thead", "tr",
    "/table", "/tbody", "/td", "/tfoot", "/th", "/thead", "/tr",
    "u", "ul", "wbr",
    "/u", "/ul", "/wbr",
]

DISALLOWED_HTML_TAG_RULE_LINK = "https://review.learn.microsoft.com/en-us/help/platform/validation-ref/disallowed-html-tag?branch=main"

BROKEN_LINK_RULE_LINK = "https://review.learn.microsoft.com/en-us/help/platform/validation-ref/other-site-link-broken?branch=main"

GLOBAL_EXCLUDE_COMMANDS = ['wait']

EXCLUDE_COMMANDS = {
    'network': [
        # No bastion to test
        'network bastion rdp',
        'network bastion ssh',
        'network bastion tunnel',
        # No dns to test
        'network dns record-set a list',
        'network dns record-set aaaa delete',
        'network dns record-set aaaa list',
        'network dns record-set aaaa show',
        'network dns record-set aaaa update',
        'network dns record-set caa delete',
        'network dns record-set caa list',
        'network dns record-set caa show',
        'network dns record-set caa update',
        'network dns record-set cname list',
        'network dns record-set cname show',
        'network dns record-set mx delete',
        'network dns record-set mx list',
        'network dns record-set mx show',
        'network dns record-set mx update',
        'network dns record-set ns delete',
        'network dns record-set ns list',
        'network dns record-set ns update',
        'network dns record-set ptr delete',
        'network dns record-set ptr list',
        'network dns record-set ptr show',
        'network dns record-set ptr update',
        'network dns record-set soa show',
        'network dns record-set srv delete',
        'network dns record-set srv list',
        'network dns record-set srv show',
        'network dns record-set srv update',
        'network dns record-set txt delete',
        'network dns record-set txt show',
        'network dns record-set txt update',
    ],
    'resource': [
        # Permission denied
        'account management-group subscription add',
        'account management-group subscription remove',
        # Hard to test
        'bicep publish',
        'feature register',
    ],
    'role': [
        # Deprecate
        'ad app permission admin-consent',
        'ad group owner remove',
        'ad signed-in-user show',
        'ad sp owner list',
        'ad user list',
        # Move identity from role module to identity module
        'identity show',
        'identity delete',
        'identity list',
        'identity list-operations',
    ],
    'vm': [
        # Hard to test
        'vm host restart',
    ]
}


GLOBAL_PARAMETERS = [
    ['--debug'],
    ['--help', '-h'],
    ['--only-show-errors'],
    ['--output', '-o'],
    ['--query'],
    ['--query-examples'],
    ['--subscription'],
    ['--verbose'],
]
GENERIC_UPDATE_PARAMETERS = [
    ['--add'],
    ['--force-string'],
    ['--remove'],
    ['--set'],
]
WAIT_CONDITION_PARAMETERS = [
    ['--created'],
    ['--custom'],
    ['--deleted'],
    ['--exists'],
    ['--interval'],
    ['--timeout'],
    ['--updated'],
]
OTHER_PARAMETERS = [
    # batch
    ['--account-name'], ['--account-key'], ['--account-endpoint'],
    ['--ids'],
    ['--ignore-errors'],
    ['--location', '-l'],
    ['--username', '-u'],
    ['--password', '-p'],
    ['--name', '-n'],
    ['--no-wait'],
    ['--resource-group', '-g'],
    ['--tags'],
    ['--yes', '-y'],
]


CMD_PATTERN = [
    # self.cmd( # test.cmd(
    r'.\w{0,}cmd\(\n',
    # self.cmd('xxxx or self.cmd("xxx or test.cmd(' or fstring
    r'.\w{0,}cmd\(f?(?:\'|")(.*)(?:\'|")',
    # xxxcmd = '' or xxxcmd = "" or xxxcmd1 or ***Command or ***command or fstring
    r'(?:cmd|command|Command)\d* = f?(?:\'|"){1}([a-z]+.*)(?:\'|"){1}',
    # r'self.cmd\(\n', r'cmd = (?:\'|")(.*)(?:\'|")(.*)?',
    # xxxcmd = """ or xxxcmd = ''' or xxxcmd1
    r'cmd\d* = (?:"{3}|\'{3})(.*)',
]
# Match content in '' or ""
QUO_PATTERN = r'(["\'])((?:\\\1|(?:(?!\1)).)*)(\1)'
# Match end: ) or checks= or ,\n
END_PATTERN = r'(\)|checks=|,\n)'
# Match doc string ''' or """
DOCS_END_PATTERN = r'"{3}$|\'{3}$'
# Match start with ' or "
NOT_END_PATTERN = r'^(\s)+(\'|")'
# (# xxxx)
NUMBER_SIGN_PATTERN = r'^\s*#.*$'

RED = 'red'
ORANGE = 'orange'
GREEN = 'green'
BLUE = 'blue'
GOLD = 'gold'

RED_PCT = 30
ORANGE_PCT = 60
GREEN_PCT = 80
BLUE_PCT = 100

VERSION_MAJOR_TAG = "major"
VERSION_MINOR_TAG = "minor"
VERSION_PATCH_TAG = "patch"
VERSION_PRE_TAG = "pre"

VERSION_STABLE_TAG = "stable"
VERSION_PREVIEW_TAG = "preview"

PREVIEW_INIT_SUFFIX = "b1"

CLI_EXTENSION_INDEX_URL = "https://azcliextensionsync.blob.core.windows.net/index1/index.json"

CMD_EXAMPLE_CONFIG_FILE = "./data/cmd_example_config.json"
CMD_EXAMPLE_CONFIG_FILE_PATH = f"{os.path.dirname(os.path.realpath(__file__))}/linter/{CMD_EXAMPLE_CONFIG_FILE}"
CMD_EXAMPLE_CONFIG_FILE_URL = "https://azcmdchangemgmt.blob.core.windows.net/azure-cli-dev-tool-config/cmd_example_config.json"
CMD_EXAMPLE_DEFAULT = 1
