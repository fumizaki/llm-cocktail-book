from typing import Optional
import bcrypt


class HashingClient:

    def __init__(self, salt: Optional[str] = bcrypt.gensalt().decode(), stretching: Optional[int] = 10) -> None:
        self.salt: str = salt
        self.stretching: int = stretching


    def hash(self, input: str) -> str:
        try:
            for _ in range(self.stretching):
                _hashed: bytes = bcrypt.hashpw(
                    input.encode(),
                    self.salt.encode(),
                )
                input = _hashed.decode()
            return _hashed.decode()
        
        except:
            raise ValueError(f"Invalid hashing")


    def verify(self, hashed: str, input: str) -> bool:
        try:
            for _ in range(self.stretching):
                _hashed: bytes = bcrypt.hashpw(
                    input.encode(),
                    self.salt.encode(),
                )
                input = _hashed.decode()
            return hashed == input
        
        except:
            raise ValueError(f"Invalid hash verification")