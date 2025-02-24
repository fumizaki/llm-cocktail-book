from .text_generation_model import TextGenerationMessage, TextGenerationMode

def context_to_prompt(context: list[TextGenerationMessage]) -> str:
    prompt = ''

    messages = context[::-1]
    for message in messages:
        prompt += f"{message.role}: {message.content}"

    return prompt

TEXT_GENERATION_PROMPT = """\
"""

DISCUSSION_PROMPT = """\
## Steps

1. Carefully analyze the text.
2. Proceed to generate the text into text.

"""

CODE_PROMPT = """\
## Steps

1. Carefully analyze the text.
2. Proceed to generate the text into text.

"""

def build_specialized_prompt(mode: TextGenerationMode) -> str:
    prompt = TEXT_GENERATION_PROMPT
    if mode == TextGenerationMode.DISCUSSION:
        return prompt + DISCUSSION_PROMPT
    elif mode == TextGenerationMode.CODE:
        return prompt + CODE_PROMPT
    else:
        return prompt

