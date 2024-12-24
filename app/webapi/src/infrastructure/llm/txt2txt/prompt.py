from .model import Txt2TxtLLMMessage


def build_contextualized_prompt(context: list[Txt2TxtLLMMessage]) -> str:
    prompt = ''

    context = context[::-1]
    for message in context:
        prompt += f"{message.role}: {message.prompt}"

    return prompt