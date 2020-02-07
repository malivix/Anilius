import platform

import click
from grpc import __version__ as grpc_version
from sqlalchemy import __version__ as sqlalchemy_version


def get_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    from anilius import __version__

    message = "Python %(python)s\nAnilius %(anilius)s\ngRPC %(grpc)s\nSQLAlchemy %(sqlalchemy)s"
    click.echo(
        message
        % {
            "python": platform.python_version(),
            "anilius": __version__,
            "grpc": grpc_version,
            "sqlalchemy": sqlalchemy_version,
        },
        color=ctx.color,
    )
    ctx.exit()


version_option = click.Option(
    ["--version"],
    help="Show the anilius version",
    expose_value=False,
    callback=get_version,
    is_flag=True,
    is_eager=True,
)
