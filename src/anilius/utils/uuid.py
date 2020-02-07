import re

UUID4_PATTERN = (
    "^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)


def validate_uuid4(uid):
    uid = str(uid)
    return bool(re.match(UUID4_PATTERN, uid))
