from .model import Txt2VecModel, Txt2VecResult, Txt2VecLLM
from .prompt import split_prompt
from src.infrastructure.llm.openai.embeddings import AsyncOpenAIEmbeddingsClient, OpenAIEmbeddingsModel, OpenAIEmbeddingsResult

class LLMTxt2VecClient:
    def __init__(self) -> None:
        pass

    async def generate(self, params: Txt2VecModel) -> Txt2VecResult:
        try:
            chunks = split_prompt(params.prompt)

    
            result: Txt2VecResult
            if params.meta.llm == Txt2VecLLM.OPENAI:
                client = AsyncOpenAIEmbeddingsClient()
                res = await client.vectorize(
                    OpenAIEmbeddingsModel(
                        input=chunks,
                        model='text-embedding-3-small'
                        )
                    )
                
                result = Txt2VecResult(
                    llm=Txt2VecLLM.OPENAI,
                    model=res.model,
                    usage=res.usage,
                    chunks=chunks,
                    vector=res.vector
                )
                
            
            return result
        except Exception as e:
            print(f"Error during embedding generation: {e}")