import pytest
import bcrypt
from src.infrastructure.hashing import HashingClient  # your_module を適切なモジュール名に修正


SALT_STR = bcrypt.gensalt().decode() # テスト用の固定salt(str)

def test_hashing_client_init():
    client = HashingClient(salt=SALT_STR)
    assert client.salt == SALT_STR
    assert client.stretching == 10

    client_custom = HashingClient(salt=SALT_STR, stretching=5)
    assert client_custom.stretching == 5

def test_hashing_client_hash():
    client = HashingClient(salt=SALT_STR)
    input_str = "test_password"
    hashed_str = client.hash(input_str)
    assert isinstance(hashed_str, str)
    assert hashed_str != input_str

def test_hashing_client_verify():
    client = HashingClient(salt=SALT_STR)
    input_str = "test_password"
    hashed_str = client.hash(input_str)
    assert client.verify(hashed_str, input_str)

def test_hashing_client_verify_incorrect():
    client = HashingClient(salt=SALT_STR)
    input_str = "test_password"
    incorrect_input = "wrong_password"
    hashed_str = client.hash(input_str)
    assert not client.verify(hashed_str, incorrect_input)

def test_hashing_client_hash_empty_input():
    client = HashingClient(salt=SALT_STR)
    input_str = ""
    hashed_str = client.hash(input_str)
    assert isinstance(hashed_str, str)

def test_hashing_client_verify_empty_input():
    client = HashingClient(salt=SALT_STR)
    input_str = ""
    hashed_str = client.hash(input_str)
    assert client.verify(hashed_str, input_str)

def test_hashing_client_unicode():
    client = HashingClient(salt=SALT_STR)
    input_str = "日本語のパスワード"
    hashed_str = client.hash(input_str)
    assert client.verify(hashed_str, input_str)