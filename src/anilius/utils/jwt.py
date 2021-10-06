import jwt

from anilius.core.settings import settings


def encode_jwt(claim):
    return jwt.encode(claim, settings.get("JWT_SECRET", ""), algorithm="HS512")


def decode_jwt(encoded):
    return jwt.decode(encoded, settings.get("JWT_SECRET", ""), algorithms=["HS512"])
