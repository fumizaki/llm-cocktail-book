from enum import Enum
from pydantic import BaseModel



class ProgrammingLanguage(str, Enum):
    PYTHON = 'python'


class CodeGenerationResponseFormat(BaseModel):
    content: str
    test: str