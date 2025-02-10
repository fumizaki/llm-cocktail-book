from .txt2vec_model import Txt2VecModel, Txt2VecResult, Txt2VecResource
from .txt2vec_prompt import split_prompt
from .resource.openai import AsyncOpenAIEmbeddingsClient, OpenAIEmbeddingsModel, OpenAIEmbeddingsResult


class Txt2VecClient:
    def __init__(self) -> None:
        pass

    async def generate(self, params: Txt2VecModel) -> Txt2VecResult:
        try:
            chunks = split_prompt(params.prompt)

            result: Txt2VecResult
            if params.meta.resource == Txt2VecResource.OPENAI:
                client = AsyncOpenAIEmbeddingsClient()
                res = await client.vectorize(
                    OpenAIEmbeddingsModel(
                        prompt=chunks,
                        model='text-embedding-3-small'
                        )
                    )
                
                result = Txt2VecResult(
                    resource=Txt2VecResource.OPENAI,
                    model=res.model,
                    usage=res.usage,
                    chunks=chunks,
                    vector=res.vector
                )
                
            return result
        except Exception as e:
            print(f"Error during embedding generation: {e}")