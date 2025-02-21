from enum import Enum
from pydantic import BaseModel


class Txt2TxtMessageRole(str, Enum):
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
    USER = 'user'


class Txt2TxtMessage(BaseModel):
    prompt: str
    role: Txt2TxtMessageRole


class Txt2TxtResource(str, Enum):
    OPENAI = 'openai'
    GOOGLE = 'google'
    ANTHROPIC = 'anthropic'


class GenerationMode(str, Enum):
    DISCUSSION = 'discussion'
    CODE = 'code'
    # TODO: PROMPT = 'prompt'
    # TODO: TRANSLATION = 'translation'
    # TODO: SUMMARY = 'summary'
    

class Txt2TxtResult(BaseModel):
    resource: Txt2TxtResource
    model: str
    usage: int
    content: str