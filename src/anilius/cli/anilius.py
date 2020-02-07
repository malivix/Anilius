import os

import click
from anilius.cli.version import version_option


class AniliusGroup(click.Group):
    """Special subclass of the :class:`AppGroup` group that supports
    loading more commands from the configured Anilius app.  Normally a
    developer does not have to interface with this class but there are
    some very advanced use cases for which it makes sense to create an
    instance of this.
    For information as of why this is useful see :ref:`custom-scripts`.
    :param add_default_commands: if this is True then the default run and
        shell commands will be added.
    :param add_version_option: adds the ``--version`` option.
    :param create_app: an optional callback that is passed the script info and
        returns the loaded app.
    :param load_dotenv: Load the nearest :file:`.env` and :file:`.flaskenv`
        files to set environment variables. Will also change the working
        directory to the directory containing the first file found.
    :param set_debug_flag: Set the app's debug flag based on the active
        environment
    .. versionchanged:: 1.0
        If installed, python-dotenv will be used to load environment variables
        from :file:`.env` and :file:`.flaskenv` files.
    """

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
Provides commands from Anilius, extensions, and the application. Loads the
application defined in the ANILIUS_APP environment variable.
Setting the ANILIUS_ENV environment variable to 'development' will enable
debug mode.
\n
  {prefix}{cmd} ANILIUS_APP=hello.py\n
  {prefix}{cmd} ANILIUS_ENV=development\n
  {prefix}anilius run\n
""".format(
        cmd="export" if os.name == "posix" else "set",
        prefix="$ " if os.name == "posix" else "> ",
    )
)
