import click


def create():
    pass


create_command = click.Command(
    "create",
    help="Create entities of anilius",
    callback=create,
)
