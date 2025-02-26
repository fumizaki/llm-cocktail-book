from typing import Union, Optional
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
    """
    テキストをベクトル化するクライアント。
    """
    
    def __init__(
        self,
        resource: VectorGenerationResource,
    ) -> None:
        super().__init__()
        self.resource: VectorGenerationResource = resource
        self.model = self.get_default_model()
        
    def get_default_model(self) -> str:
        models = {
            VectorGenerationResource.OPENAI: "text-embedding-3-large",
        }
        return models.get(self.resource)
    
    def get_api_key(self) -> str:
        api_keys = {
            VectorGenerationResource.OPENAI: self._openai_api_key,
        }
        return api_keys.get(self.resource)
    
    def get_client(
        self,
        resource: Optional[VectorGenerationResource] = None,
        model: Optional[str] = None
    ) -> Union[OpenAIEmbeddings]:
        # `resource` が指定されていれば設定
        if resource:
            self.resource = resource

        # `model` が指定されていれば設定
        if model:
            self.model = model

        if self.resource == VectorGenerationResource.OPENAI:
            return OpenAIEmbeddings(
                api_key=self.get_api_key(),
                model=self.model,
                )
        else:
            raise ValueError('Unsupported resource')

    @staticmethod
    def split_by_character(
        text: str,
        delimiter: str = "\n\n",
        is_delimiter_regex: bool = False,
        size: int = 1000,
        overlap: int = 200
    ) -> list[str]:
        """
        文字単位でテキストを分割する。
        
        Args:
            text (str): 分割対象のテキスト。
            delimiter (str): 分割に使用する文字。
            is_delimiter_regex (bool): 区切り文字を正規表現として扱うか。
            size (int): 各チャンクの最大サイズ。
            overlap (int): チャンク間のオーバーラップサイズ。

        Returns:
            list[str]: 分割されたテキストリスト。
        """
        splitter = CharacterTextSplitter(
            separator=delimiter,
            is_separator_regex=is_delimiter_regex,
            chunk_size=size,
            chunk_overlap=overlap,
        )
        return splitter.split_text(text)

    @staticmethod
    def recursively_split_by_character(
        text: str,
        delimiters: list[str] = ["\n\n"],
        is_delimiter_regex: bool = False,
        size: int = 1000,
        overlap: int = 200
    ) -> list[str]:
        """
        再帰的にテキストを分割する。
        
        Args:
            text (str): 分割対象のテキスト。
            delimiters (list[str]): 分割に使用する文字のリスト。
            is_delimiter_regex (bool): 区切り文字を正規表現として扱うか。
            size (int): 各チャンクの最大サイズ。
            overlap (int): チャンク間のオーバーラップサイズ。

        Returns:
            list[str]: 分割されたテキストリスト。
        """
        splitter = RecursiveCharacterTextSplitter(
            separators=delimiters,
            is_separator_regex=is_delimiter_regex,
            chunk_size=size,
            chunk_overlap=overlap,
        )
        return splitter.split_text(text)

    async def generate(
            self,
            text: str,
            resource: Optional[VectorGenerationResource] = None,
            model: Optional[str] = None
        ) -> VectorGenerationResponse:
        """
        テキストをベクトル化する。
        
        Args:
            text (str): ベクトル化対象のテキスト。
        
        Returns:
            VectorGenerationResponse: 生成されたベクトル情報。
        """
        if not text.strip():
            raise ValueError("Input text cannot be empty.")

        try:
            client = self.get_client(resource, model)
            res = await client.aembed_query(text=text)
            return VectorGenerationResponse(
                resource=self.resource,
                model=self.model,
                content=text,
                vector=res,
            )
        except Exception as e:
            raise RuntimeError(f"Error in vector generation: {str(e)}")
