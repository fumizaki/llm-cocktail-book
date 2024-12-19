from src.application.core.model import CoreModel
from src.domain.type.llm import Message, ProgrammingLanguage

class Txt2CodeModel(CoreModel):
    language: ProgrammingLanguage
    prompt: str
    context: list[Message]


