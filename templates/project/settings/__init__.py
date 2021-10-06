import os

env = os.environ.get("STAGE", "dev")

if env == "production":
    from settings.production import *
else:
    from settings.dev import *
