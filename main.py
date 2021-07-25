from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel
from rst_to_myst import rst_to_myst

app = FastAPI()


class InputReST(BaseModel):
    text: str


@app.get("/")
async def home():
    return {"message": "Hello, world!"}


@app.post("/convert")
async def convert(input_rest: InputReST):
    output = rst_to_myst(
        input_rest.text,
        use_sphinx=False,
    )
    return {"input_rest": input_rest, "output_myst": output.text}
