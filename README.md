# MySTyc

Online conversor of reStructuredText to MyST.

## Installation

```bash
(.venv) $ pip install -r requirements.txt
```

or, alternatively,

```bash
(.venv) $ pip-sync
```

## Usage

```bash
$ curl -s -H "Content-Type: application/json" -d '{"text": "Title\n-----\n\nHello world"}' -XPOST http://localhost:8000/convert | jq
{
  "input_rest": {
    "text": "Title\n-----\n\nHello world"
  },
  "output_myst": "# Title\n\nHello world\n"
}
$ curl -s -H "Content-Type: application/json" -d '{"text": "Title\n-----\n\nHello world"}' -XPOST http://localhost:8000/convert | jq '.output_myst' | xargs -I{} printf {}
# Title

Hello world
```
