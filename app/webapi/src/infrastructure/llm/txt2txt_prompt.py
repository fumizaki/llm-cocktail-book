from .txt2txt_model import Txt2TxtMessage
from typing import Optional

def gen_context(messages: list[Txt2TxtMessage]) -> str:
    prompt = ''

    messages = messages[::-1]
    for message in messages:
        prompt += f"{message.role}: {message.prompt}"

    return prompt


DISCUSSION = """\
# Steps

1. Carefully analyze the text.
2. Proceed to generate the text into text.

"""

CODE = """\
# Task

Generate Only Python code based on the provided text description. The code should be executable and, where appropriate, include basic error handling or input validation.

# Instructions

1. Carefully analyze the input text description to understand the desired functionality.
2. Generate efficient and readable Python code that fulfills the description.
3. If applicable, generate corresponding test code using testing code.
"""


def gen_discussion() -> str:
    prompt = DISCUSSION
    return prompt


def gen_code() -> str:
    prompt = CODE
    return prompt



