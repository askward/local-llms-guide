from fastapi import FastAPI
from fastapi.responses import JSONResponse, StreamingResponse
from ollama import AsyncClient
from pydantic import BaseModel
import json
import os


class Request(BaseModel):
    history: list


model_name = os.environ["LLM"]
ollama_client = AsyncClient(host=os.environ["OLLAMA_BASE_URL"])
app = FastAPI()


@app.get("/")
def read_root():
    return JSONResponse(content={"status": "healthy"})


@app.post("/generate")
async def generate(request: Request):
    try:
        response = await ollama_client.chat(model=model_name, messages=request.history)
        return JSONResponse(content=response)
    except Exception as e:
        error_json = {"message": {"content": f"ERROR : {e}"}}
        return JSONResponse(content=error_json, status_code=500)


async def stream_from_ollama(request: Request):
    try:
        async for part in await ollama_client.chat(model=model_name, messages=request.history, stream=True):
            yield json.dumps(part)
    except Exception as e:
        error_json = {"message": {"content": f"ERROR : {e}"}}
        yield json.dumps(error_json)


@app.post("/stream")
async def stream(request: Request):
    return StreamingResponse(content=stream_from_ollama(request=request), media_type="application/json")
