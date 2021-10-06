import os

DEBUG = True

DATABASE_URI = os.environ.get(
    "DATABASE_URI", "mysql://root:wallet@127.0.0.1:3306/wallet"
)
DATABASE_CONNECT_OPTIONS = {}
SENTRY_DSN = ""
JWT_SECRET = "sagasg49thsd9uvh0348gupsadgjw"

ENABLE_MODULES = ("users",)
