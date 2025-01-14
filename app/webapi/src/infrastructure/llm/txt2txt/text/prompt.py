from typing import Optional
from .model import Language

GENERAL_PROMPT = """\
# Steps

1. Carefully analyze the text.
2. Proceed to generate the text into text.

"""

def build_text_prompt(lang: Optional[Language]) -> str:
    prompt = ''
    if lang is None:
        prompt += GENERAL_PROMPT
    
    return prompt