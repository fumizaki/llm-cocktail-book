from .model import Txt2VecModel, Txt2VecResult, Txt2VecLLM
from .prompt import split_prompt
from src.infrastructure.llm.openai.embeddings import AsyncOpenAIEmbeddingsClient, OpenAIEmbeddingsModel, OpenAIEmbeddingsResult

class LLMTxt2VecClient:
    def __init__(self) -> None:
        pass

    async def generate(self, params: Txt2VecModel) -> Txt2VecResult:
        try:
            chunks = split_prompt(params.prompt)

            model = ''
            vec: list[list[float]] = []
            usage: int = 0

            if params.meta.llm == Txt2VecLLM.OPENAI:
                client = AsyncOpenAIEmbeddingsClient()
                for chunk in chunks:
                    res = await client.vectorize(
                            input=chunk,
                            model='text-embedding-3-small'
                        )
                    model = res.model
                    vec.append(res.content)
                    usage += res.usage
            
            return Txt2VecResult(
                model=model,
                usage=usage,
                vector=vec
            )
        except Exception as e:
            print(f"Error during embedding generation: {e}")