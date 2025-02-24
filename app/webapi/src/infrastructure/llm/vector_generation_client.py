from .generation_client import GenerationClient
from .vector_generation_model import (
    VectorGenerationResponse,
    VectorGenerationResource,

)
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)

class VectorGenerationClient(GenerationClient):
    
    def __init__(
            self,
            resource: VectorGenerationResource,
        ) -> None:
        super().__init__()
        self.resource: VectorGenerationResource = resource
        if self.resource == VectorGenerationResource.OPENAI:
            self.model: str = 'text-embedding-3-large'
            self.client: OpenAIEmbeddings = OpenAIEmbeddings(
                api_key=self._openai_api_key,
                model=self.model,
                )
        else:
            raise
    
    # https://zenn.dev/buenotheebiten/articles/af5cfba98b1b8f#1.-split-by-character
    @staticmethod
    def split_by_character(text: str, delimiter: str = "\n\n", is_delimiter_regex: bool = False, size: int = 1000, overlap: int = 200) -> list[str]:
        splitter = CharacterTextSplitter(
            separator=delimiter,
            is_separator_regex=is_delimiter_regex,
            chunk_size=size,
            chunk_overlap=overlap
        )
        return splitter.split_text(text)

    # https://zenn.dev/buenotheebiten/articles/af5cfba98b1b8f#2.-recursively-split-by-character
    @staticmethod
    def recursively_split_with_length(text: str, delimiters: str = ["\n\n"], is_delimiter_regex: bool = False, size: int = 1000, overlap: int = 200) -> list[str]:
        splitter = RecursiveCharacterTextSplitter(
            separators=delimiters,
            is_separator_regex=is_delimiter_regex,
            chunk_size=size,
            chunk_overlap=overlap
        )
        return splitter.split_text(text)

    # TODO: https://zenn.dev/buenotheebiten/articles/af5cfba98b1b8f#3.-recursively-split-json
    # TODO: https://zenn.dev/buenotheebiten/articles/af5cfba98b1b8f#4.-htmlheadertextsplitter
    # TODO: https://zenn.dev/buenotheebiten/articles/af5cfba98b1b8f#5.-markdownheadertextsplitter

    async def generate(self, text: str) -> VectorGenerationResponse:
        try:
            res = await self.client.aembed_query(text=text)
            return VectorGenerationResponse(
                resource=self.resource,
                model=self.model,
                content=text,
                vector=res
            )
        except Exception as e:
            raise