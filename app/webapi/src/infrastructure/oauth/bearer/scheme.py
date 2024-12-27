from .exception import InvalidBearerTokenError

def parse_bearer_token(authorization: str) -> str:
        """
        Authorization headerからBearer tokenを抽出

        Args:
            authorization (str): Authorization header値

        Returns:
            str: Bearer token

        Raises:
            InvalidBearerTokenError: Bearer tokenが不正な場合
        """
        scheme, _, param = authorization.partition(" ")
        if scheme.lower() != "bearer":
            raise InvalidBearerTokenError("Invalid authorization scheme")
        if not param:
            raise InvalidBearerTokenError("Token is missing")
        return param
