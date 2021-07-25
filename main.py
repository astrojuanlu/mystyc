from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from rst_to_myst import rst_to_myst

app = FastAPI()
templates = Jinja2Templates(directory="templates")


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


@app.get("/convert", response_class=HTMLResponse)
async def convert(request: Request):
    return templates.TemplateResponse("convert.html", {"request": request})
