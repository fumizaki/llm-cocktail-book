import bcrypt

class HashClient:

    @staticmethod
    def create_salt() -> str:
        return bcrypt.gensalt().decode()
    
    @staticmethod
    def create_stretching() -> int:
        return 10


    @staticmethod
    def hash(input: str, salt: str, stretching: int = 1) -> str:
        try:
            for _ in range(stretching):
                _hashed: bytes = bcrypt.hashpw(
                    input.encode(),
                    salt.encode(),
                )
                input = _hashed.decode()
            return _hashed.decode()
        
        except:
            raise ValueError(f"Invalid hashing")


    @staticmethod
    def verify(hashed: str, input: str, salt: str, stretching: int = 1) -> bool:
        try:
            for _ in range(stretching):
                _hashed: bytes = bcrypt.hashpw(
                    input.encode(),
                    salt.encode(),
                )
                input = _hashed.decode()
            return hashed == input
        
        except:
            raise ValueError(f"Invalid hash verification")