from typing import Optional
from src.domain.schema.core import CoreSchema


class Txt2TxtRequestParams(CoreSchema):
    prompt: str