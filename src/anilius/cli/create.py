import click


def create():
    pass


serve_command = click.Command(
    "create",
    help="Create entities of anilius",
    callback=create,
)
