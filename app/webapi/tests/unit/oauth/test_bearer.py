import pytest
from src.infrastructure.oauth import parse_bearer_token, InvalidBearerTokenError

def test_parse_bearer_token_valid():
    authorization = "Bearer test_token"
    token = parse_bearer_token(authorization)
    assert token == "test_token"

def test_parse_bearer_token_case_insensitive():
    authorization = "bearer test_token"
    token = parse_bearer_token(authorization)
    assert token == "test_token"

    authorization = "BEARER test_token"
    token = parse_bearer_token(authorization)
    assert token == "test_token"

def test_parse_bearer_token_no_bearer():
    authorization = "Basic test_token"
    with pytest.raises(InvalidBearerTokenError) as excinfo:
        parse_bearer_token(authorization)
    assert str(excinfo.value) == "Invalid authorization scheme"

def test_parse_bearer_token_no_token():
    authorization = "Bearer "
    with pytest.raises(InvalidBearerTokenError) as excinfo:
        parse_bearer_token(authorization)
    assert str(excinfo.value) == "Token is missing"

def test_parse_bearer_token_empty_string():
    authorization = ""
    with pytest.raises(InvalidBearerTokenError) as excinfo:
        parse_bearer_token(authorization)
    assert str(excinfo.value) == "Invalid authorization scheme"

def test_parse_bearer_token_only_space():
    authorization = " "
    with pytest.raises(InvalidBearerTokenError) as excinfo:
        parse_bearer_token(authorization)
    assert str(excinfo.value) == "Invalid authorization scheme"

