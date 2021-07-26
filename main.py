from __future__ import annotations

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from rst_to_myst import rst_to_myst

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/convert")
async def convert(input_rest: str = Form(...)):
    output = rst_to_myst(
        input_rest,
        use_sphinx=False,
    )
    return {"input_rest": input_rest, "output_myst": output.text}


@app.get("/", response_class=HTMLResponse)
async def convert(request: Request):
    return templates.TemplateResponse("convert.html", {"request": request})
