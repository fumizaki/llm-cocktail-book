from .text import build_text_prompt
from .code import build_code_prompt, CodeGenerationResponseFormat
from .model import Txt2TxtModel, Txt2TxtResult, GenerationMode, Txt2TxtLLM
from .prompt import build_contextualized_prompt
from src.infrastructure.llm.openai.chat import AsyncOpenAIChatClient
from src.infrastructure.llm.openai.chat import OpenAIChatModel, OpenAIChatMessage, OpenAIChatMessageRole



class LLMTxt2TxtClient:
    def __init__(self) -> None:
        pass

    async def generate(self, params: Txt2TxtModel) -> Txt2TxtResult:

        system_prompt: str = ''
        if params.meta.mode == GenerationMode.TEXT:
            system_prompt += build_text_prompt()
        elif params.meta.mode == GenerationMode.CODE:
            system_prompt += build_code_prompt(params.meta.lang)

        system_prompt += build_contextualized_prompt(params.context)
        
        result: Txt2TxtResult
        if params.meta.llm == Txt2TxtLLM.OPENAI:
            client = AsyncOpenAIChatClient()
            res = await client.chat(
                OpenAIChatModel(
                    model='o1-mini',
                    messages=[
                        OpenAIChatMessage(content=system_prompt, role=OpenAIChatMessageRole.ASSISTANT),
                        OpenAIChatMessage(content=params.prompt, role=OpenAIChatMessageRole.USER)
                    ],
                )
            )
            
            result = Txt2TxtResult(
                llm=Txt2TxtLLM.OPENAI,
                model=res.model,
                usage=res.usage,
                content=res.content
            )
        return result
    
"2つの整数を引数とし、引数のうち小さい方から大きい方まで加算し、最後にnで割るコードを生成してください"