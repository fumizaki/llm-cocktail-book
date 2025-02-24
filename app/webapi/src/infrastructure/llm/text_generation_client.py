from .generation_client import GenerationClient
from .text_generation_model import (
    TextGenerationResponse,
    TextGenerationResource,
    TextGenerationMode,
    TextGenerationMessage,
)
from .text_generation_prompt import context_to_prompt, build_specialized_prompt
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, AIMessage
from langchain_core.language_models.base import LanguageModelInput

class TextGenerationClient(GenerationClient):
    
    def __init__(
            self,
            resource: TextGenerationResource,
            mode: TextGenerationMode,
            context: list[TextGenerationMessage]
        ) -> None:
        super().__init__()
        self.resource: TextGenerationResource = resource
        self.mode: TextGenerationMode = mode
        if self.resource == TextGenerationResource.OPENAI:
            self.model: str = 'o1-mini'
            self.client: ChatOpenAI = ChatOpenAI(
                api_key=self._openai_api_key,
                model=self.model,
                )
            
        elif self.resource == TextGenerationResource.ANTHROPIC:
            self.model: str = 'claude-3-5-sonnet-latest'
            self.client: ChatAnthropic = ChatAnthropic(
                api_key=self._anthropic_api_key,
                model=self.model
                )
        
        elif self.resource == TextGenerationResource.GOOGLE:
            self.model: str = 'gemini-pro'
            self.client: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
                api_key=self._google_api_key,
                model=self.model
                )
        else:
            raise
        self.system_prompt: str = build_specialized_prompt(self.mode) + context_to_prompt(context)


    async def generate(self, content: LanguageModelInput):
        try:
            res = await self.client.ainvoke(
                [
                    AIMessage(content=self.system_prompt), # TODO: AIMessage -> ???
                    HumanMessage(content=content),
                ]
            )
            return TextGenerationResponse(
                resource=self.resource,
                model=self.model,
                content=res.text()
            )

        except Exception as e:
            raise