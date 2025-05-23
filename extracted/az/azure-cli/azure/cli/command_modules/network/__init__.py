# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

import azure.cli.command_modules.network._help  # pylint: disable=unused-import


class NetworkCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core import ModExtensionSuppress
        from azure.cli.core.commands import CliCommandType
        network_custom = CliCommandType(operations_tmpl='azure.cli.command_modules.network.custom#{}')
        super().__init__(
            cli_ctx=cli_ctx,
            custom_command_type=network_custom,
            suppress_extension=[
                ModExtensionSuppress(
                    __name__, 'dns', '0.0.2',
                    reason='These commands are now in the CLI.',
                    recommend_remove=True),
                ModExtensionSuppress(
                    __name__, 'express-route', '0.1.3',
                    reason='These commands are now in the CLI.',
                    recommend_remove=True)
            ]
        )

    def load_command_table(self, args):
        from azure.cli.command_modules.network.commands import load_command_table
        from azure.cli.core.aaz import load_aaz_command_table
        try:
            from . import aaz
        except ImportError:
            aaz = None
        if aaz:
            load_aaz_command_table(
                loader=self,
                aaz_pkg_name=aaz.__name__,
                args=args
            )
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azure.cli.command_modules.network._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = NetworkCommandsLoader
