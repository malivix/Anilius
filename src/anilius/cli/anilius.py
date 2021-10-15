import os

import click
from anilius.cli.create import create_command
from anilius.cli.serve import serve_command
from anilius.cli.version import version_option


class AniliusGroup(click.Group):
    def __init__(
            self,
            create_app=None,
            add_version_option=True,
            load_dotenv=True,
            set_debug_flag=True,
            **extra
    ):
        params = list(extra.pop("params", None) or ())

        if add_version_option:
            params.append(version_option)

        click.Group.__init__(self, params=params, **extra)

        self.add_command(create_command)
        self.add_command(serve_command)

        self.create_app = create_app
        self.load_dotenv = load_dotenv
        self.set_debug_flag = set_debug_flag

        self._loaded_plugin_commands = False

    def main(self, *args, **kwargs):
        os.environ["ANILIUS_RUN_FROM_CLI"] = "true"

        kwargs.setdefault("auto_envvar_prefix", "ANILIUS")
        return super(AniliusGroup, self).main(*args, **kwargs)


cli = AniliusGroup(
    help="""\
A general utility script for Anilius microservice.
""".format(
        cmd="export" if os.name == "posix" else "set",
        prefix="$ " if os.name == "posix" else "> ",
    )
)
