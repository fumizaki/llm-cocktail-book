import re
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_with_length(text: str, size: int, overlap: int) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=size,
        chunk_overlap=overlap
    )
    splitter.create_documents([text])


def split_with_delimiter(text: str, delimiters: list[str] | None = ['\n']) -> list[str]:
    """
    delimiters: list[str] | None = ['\n', ',', '.', '、', '。']
    """
    pattern = '|'.join(map(re.escape, delimiters))
    return [chunk.strip() for chunk in re.split(pattern, text) if chunk.strip()]
