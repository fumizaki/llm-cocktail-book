import base64
import magic
from typing import Union, Optional
from .generation_client import GenerationClient
from .text_generation_model import (
    TextGenerationResponse,
    TextGenerationResource,
    TextGenerationMode,
    TextGenerationMessage,
)
from .text_generation_prompt import build_specialized_prompt
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, AIMessage


class TextGenerationClient(GenerationClient):
    """
    テキスト・画像・音声データを適切な LLM に送信し、生成結果を取得するクライアント
    """

    def __init__(
        self,
        resource: TextGenerationResource,
        mode: TextGenerationMode,
        context: list[TextGenerationMessage]
    ) -> None:
        super().__init__()
        self.resource: TextGenerationResource = resource
        self.model = self.get_default_model()
        self.mode: TextGenerationMode = mode
        self.system_prompt: str = build_specialized_prompt(self.mode) + self.build_context(context)

    def build_context(self, context: list[TextGenerationMessage]) -> str:
        prompt = ''

        messages = context[::-1]
        for message in messages:
            prompt += f"{message.role}: {message.content}"

        return prompt

    def get_default_model(self) -> str:
        models = {
            TextGenerationResource.OPENAI: "o1-mini",
            TextGenerationResource.ANTHROPIC: "claude-3-7-sonnet-latest",
            TextGenerationResource.GOOGLE: "gemini-2.0-flash",
        }
        return models.get(self.resource)
    
    def get_image_model(self) -> str:
        models = {
            TextGenerationResource.OPENAI: "gpt-4o",
            TextGenerationResource.GOOGLE: "gemini-2.0-flash",
        }
        return models.get(self.resource)
    
    def get_audio_model(self) -> str:
        models = {
            TextGenerationResource.GOOGLE: "gemini-2.0-flash",
        }
        return models.get(self.resource)


    def get_api_key(self) -> str:
        api_keys = {
            TextGenerationResource.OPENAI: self._openai_api_key,
            TextGenerationResource.ANTHROPIC: self._anthropic_api_key,
            TextGenerationResource.GOOGLE: self._google_api_key,
        }
        return api_keys.get(self.resource)

    def get_client(
        self,
        content: list[Union[str, bytes]],
        resource: Optional[TextGenerationResource] = None,
        model: Optional[str] = None
    ) -> Union[ChatOpenAI, ChatAnthropic, ChatGoogleGenerativeAI]:
        """
        `content` の種類に応じて適切な `resource` と `model` を決定し、クライアントを取得する。

        - 画像が含まれる場合 → OpenAI
        - 音声が含まれる場合 → Google
        - それ以外 → 指定リソース (デフォルトは `self.resource`)

        Args:
            content (List[Union[str, bytes]]): ユーザーの入力データ
            resource (Optional[TextGenerationResource]): 使用する LLM (指定がなければ自動選択)
            model (Optional[str]): 使用するモデル (指定がなければデフォルト)

        Returns:
            Union[ChatOpenAI, ChatAnthropic, ChatGoogleGenerativeAI]: LLM クライアント
        """
        contains_image = False
        contains_audio = False

        try:
            mime_checker = magic.Magic(mime=True)  # MIME タイプ検出器
        except Exception as e:
            raise RuntimeError(f"Failed to initialize MIME detector: {str(e)}")

        for input_data in content:
            if isinstance(input_data, bytes):
                mime_type = mime_checker.from_buffer(input_data)
                if not mime_type:
                    raise ValueError("Failed to determine MIME type of input data.")
                if mime_type.startswith("image/"):
                    contains_image = True
                elif mime_type.startswith("audio/"):
                    contains_audio = True

        # `resource` が未指定なら自動選択
        if resource is None:
            if contains_image:
                # imageの場合は自動でOpenAIを利用する
                self.resource = TextGenerationResource.OPENAI
                model = self.get_image_model()
            elif contains_audio:
                # audioの場合は自動でGoogleを利用する
                self.resource = TextGenerationResource.GOOGLE
                model = self.get_audio_model()

        # `model` が指定されていれば設定
        if model:
            self.model = model

        if self.resource == TextGenerationResource.OPENAI:
            return ChatOpenAI(api_key=self.get_api_key(), model=self.model)
        elif self.resource == TextGenerationResource.ANTHROPIC:
            if contains_image or contains_audio:
                raise ValueError("Anthropic does not support image/audio input.")
            return ChatAnthropic(api_key=self.get_api_key(), model=self.model)
        elif self.resource == TextGenerationResource.GOOGLE:
            return ChatGoogleGenerativeAI(api_key=self.get_api_key(), model=self.model)


    def format_input_data(self, input_data: Union[str, bytes]) -> Union[str, dict[str, dict[str, str]]]:
        """
        入力データを適切なフォーマットに変換する。
        - 画像 → `{"type": "image_url", "image_url": { "url": f"data:{mime_type};base64,{base64_encoded}"}}`
        - 音声 → `{"type": "audio_url", "audio_url": { "url": f"data:{mime_type};base64,{base64_encoded}"}}`
        - テキスト → `{"type": "text", "text": input_data}`

        Args:
            input_data (Union[str, bytes]): 変換対象のデータ

        Returns:
            Union[str, Dict[str, Dict[str, str]]]: フォーマット済みデータ
        """
        if isinstance(input_data, str):
            return {"type": "text", "text": input_data}

        if isinstance(input_data, bytes):
            mime_checker = magic.Magic(mime=True)
            mime_type = mime_checker.from_buffer(input_data)
            if not mime_type:
                raise ValueError("Unsupported file type.")

            base64_encoded = base64.b64encode(input_data).decode("utf-8")
            if mime_type.startswith("image/"):
                return {"type": "image_url", "image_url": { "url": f"data:{mime_type};base64,{base64_encoded}"}}
            elif mime_type.startswith("audio/"):
                return {"type": "audio_url", "audio_url": { "url": f"data:{mime_type};base64,{base64_encoded}"}}
            else:
                raise ValueError("Unsupported media type.")

    async def generate(
        self,
        content: list[Union[str, bytes]],
        resource: Optional[TextGenerationResource] = None,
        model: Optional[str] = None
    ) -> TextGenerationResponse:
        """
        入力データを処理し、適切な LLM に送信して結果を取得する。

        Args:
            content (List[Union[str, bytes]]): ユーザー入力データ (テキスト、画像、音声)
            resource (Optional[TextGenerationResource]): 使用する LLM (指定がなければ自動選択)
            model (Optional[str]): 使用するモデル (指定がなければデフォルト)

        Returns:
            TextGenerationResponse: 生成結果
        """
        try:
            client = self.get_client(content, resource, model)
            messages = [AIMessage(content=self.system_prompt)]

            # for input_data in content:
            #     formatted_data = self.format_input_data(input_data)
            #     print(formatted_data)
            messages.append(HumanMessage(content=[self.format_input_data(input_data) for input_data in content]))

            response = await client.ainvoke(messages)

            return TextGenerationResponse(
                resource=self.resource,
                model=self.model,
                content=response.text()
            )

        except Exception as e:
            raise RuntimeError(f"Error in text generation: {str(e)}")
