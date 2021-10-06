from settings.common import *

SENTRY_DSN = os.environ.get("SENTRY_DSN")
DATABASE_URI = os.environ.get("DATABASE_URI")
JWT_SECRET = os.environ.get("JWT_SECRET")
