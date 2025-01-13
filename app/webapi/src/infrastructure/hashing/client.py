import bcrypt
from typing import Optional

class HashingClient:

    def __init__(self, salt: Optional[str] = None, stretching: int = 10) -> None:
        self.salt: str = salt if salt is not None else bcrypt.gensalt().decode()  # strで保存
        self.stretching: int = stretching

    def hash(self, input_str: str) -> str:
        hashed = input_str.encode()
        for _ in range(self.stretching):
            hashed = bcrypt.hashpw(hashed, self.salt.encode())  # encode()でbytesに変換
        return hashed.decode()

    def verify(self, hashed_str: str, input_str: str) -> bool:
        hashed_bytes = hashed_str.encode()
        input_bytes = input_str.encode()
        for _ in range(self.stretching):
            input_bytes = bcrypt.hashpw(input_bytes, self.salt.encode())  # encode()でbytesに変換
        return hashed_bytes == input_bytes