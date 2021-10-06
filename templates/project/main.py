#!/usr/bin/env python
import asyncio
import sys

from anilius.core.app import App

if __name__ == "__main__":
    assert sys.version_info >= (3, 6), "Project requires Python 3.7+."

    asyncio.run(App.run())
