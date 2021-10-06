import asyncio

import click
from anilius.core.app import App


def serve():
    asyncio.run(App.run())


serve_command = click.Command(
    "serve",
    help="Start anilius and serve",
    callback=serve,
)
