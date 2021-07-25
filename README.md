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
$ curl -s -d $'input_rest=Title\n-----\n\nHello world' -XPOST http://localhost:8000/convert | jq
{
  "input_rest": "Title\n-----\n\nHello world",
  "output_myst": "# Title\n\nHello world\n"
}
$ curl -s -d $'input_rest=Title\n-----\n\nHello world' -XPOST http://localhost:8000/convert | jq '.output_myst' | xargs -I{} printf {}
# Title

Hello world
```
