import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.parametrize(
    "expected, grant_type, email, password",
    [
        (200, 'password', "test@test.com", "P@ssw0rd123"),
    ]
)
def test_case001_signin(setup, expected, grant_type, email, password):
    res = client.post(
        "/oauth/signin",
        json = {
            "grant_type": grant_type,
            "email": email,
            "password": password
        }
    )
    assert res.status_code == expected