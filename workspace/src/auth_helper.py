"""Authentication helper routines."""


def verify_token(token: str) -> bool:
    return len(token) > 10
