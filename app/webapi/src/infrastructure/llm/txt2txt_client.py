from .txt2txt_prompt import gen_context, gen_discussion, gen_code
from .txt2txt_model import Txt2TxtMessage, Txt2TxtResult, GenerationMode, Txt2TxtResource
from .resource.openai import AsyncOpenAIChatClient, OpenAIChatModel, OpenAIChatMessage, OpenAIChatMessageRole
from .resource.google import AsyncGoogleAIChatClient, GoogleAIChatModel, GoogleAIChatMessage, GoogleAIChatMessageRole
from .resource.anthropic import AsyncAnthropicChatClient, AnthropicChatModel, AnthropicChatMessage, AnthropicChatMessageRole

class Txt2TxtClient:
    def __init__(self, resource: Txt2TxtResource, mode: GenerationMode) -> None:
        self.resource = resource
        self.mode = mode

    async def generate(self, prompt: str, context: list[Txt2TxtMessage]) -> Txt2TxtResult:
        try:
            system_prompt: str = ''
            if self.mode == GenerationMode.DISCUSSION:
                system_prompt += gen_discussion()
            elif self.mode == GenerationMode.CODE:
                system_prompt += gen_code()
            else:
                raise

            system_prompt += gen_context(context)

            result = Txt2TxtResult
            if self.resource == Txt2TxtResource.OPENAI:
                client = AsyncOpenAIChatClient()
                res = await client.chat(
                    OpenAIChatModel(
                        model='o1-mini',
                        messages=[
                            OpenAIChatMessage(content=system_prompt, role=OpenAIChatMessageRole.ASSISTANT),
                            OpenAIChatMessage(content=prompt, role=OpenAIChatMessageRole.USER)
                        ],
                    )
                )
                
                result = Txt2TxtResult(
                    resource=Txt2TxtResource.OPENAI,
                    model=res.model,
                    usage=res.usage,
                    content=res.content
                )

            elif self.resource == Txt2TxtResource.GOOGLE:
                client = AsyncGoogleAIChatClient()
                res = await client.chat(
                    GoogleAIChatModel(
                        model='gemini-pro',
                        contents=[
                            GoogleAIChatMessage(parts=system_prompt + prompt, role=GoogleAIChatMessageRole.USER),
                        ]
                    )
                )

                result = Txt2TxtResult(
                    resource=Txt2TxtResource.GOOGLE,
                    model=res.model,
                    usage=res.usage,
                    content=res.content
                )


            elif self.resource == Txt2TxtResource.ANTHROPIC:
                client = AsyncAnthropicChatClient()
                res = await client.chat(
                    AnthropicChatModel(
                        model='claude-3-5-sonnet-latest',
                        messages=[
                            AnthropicChatMessage(content=system_prompt, role=AnthropicChatMessageRole.ASSISTANT),
                            AnthropicChatMessage(content=prompt, role=AnthropicChatMessageRole.USER)
                        ]
                    )
                )

                result = Txt2TxtResult(
                    resource=Txt2TxtResource.ANTHROPIC,
                    model=res.model,
                    usage=res.usage,
                    content=res.content
                )
            
            else:
                raise

            return result


        except Exception as e:
            raise
