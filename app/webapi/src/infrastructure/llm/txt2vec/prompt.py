import re

def split_prompt(prompt: str, delimiters: list[str] | None = ['\n']) -> list[str]:
    """
    delimiters: list[str] | None = ['\n', ',', '.', '、', '。']
    """
    pattern = '|'.join(map(re.escape, delimiters))
    return [chunk.strip() for chunk in re.split(pattern, prompt) if chunk.strip()]
