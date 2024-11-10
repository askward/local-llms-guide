from pydantic import BaseModel
import httpx
import asyncio
import json


class Request(BaseModel):
    history: list


async def main():
    message = "Can you explain quantum computing to me?"
    request = Request(history=[{"role": "user", "content": message}])

    chat_url = "http://ollama-fastapi:1010/generate"
    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(url=chat_url, json=request.__dict__)
        response_dict = json.loads(response._content.decode("utf-8"))
        print(response_dict["message"]["content"])

    stream_url = "http://ollama-fastapi:1010/stream"
    async with httpx.AsyncClient(timeout=120) as client:
        async with client.stream('POST', url=stream_url, json=request.__dict__) as response:
            async for chunk in response.aiter_bytes():
                chunk_dict = json.loads(chunk.decode("utf-8"))
                print(chunk_dict["message"]["content"], end="")


if __name__ == "__main__":
    asyncio.run(main())