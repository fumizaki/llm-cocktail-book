from src.infrastructure.openai.chat import AsyncOpenAIChatClient
from src.infrastructure.openai.embeddings import AsyncOpenAIEmbeddingsClient
from src.infrastructure.qdrant.session import QdrantSessionClient


class GenerationUsecase:
    
    def __init__(self):
        self.params = {'collection_name': 'test'}



    async def txt2txt_exec(self, query: str):
        openai_embeddings_client = AsyncOpenAIEmbeddingsClient()
        response = await openai_embeddings_client.vectorize(prompt=query)
        qdrant_client = QdrantSessionClient()
        results = qdrant_client.search(collection_name=self.params['collection_name'], query_vector=response.vector, top_k=5)
        reference = "\n".join([f"{result.payload['chunk']}" for result in results])
        system_prompt = f"""\
                事前知識ではなく、常に提供されたコンテキスト情報を使用してクエリに回答してください。\n
                従うべきいくつかのルール:\n
                1. 回答内で指定されたコンテキストを直接参照しないでください。\n
                2. 「コンテキストに基づいて、...」や「コンテキスト情報は...」、またはそれに類するような記述は避けてください。\n
                3. 回答は1000字以内で、直接聞かれた内容だけを回答してください。\n
                4. もし回答が分からない場合は、分かりません、と回答してください。

                ---
                {reference}
                """.strip()
        
        openai_chat_client = AsyncOpenAIChatClient()
        chat_response = await openai_chat_client.chat_stream(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
        )
        
        return chat_response