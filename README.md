# MySTyc

Online conversor of reStructuredText to MyST. Try it live here:

https://mystyc.herokuapp.com/

## Installation

```bash
(.venv) $ pip install -r requirements.txt
```

or, alternatively,

```bash
(.venv) $ pip-sync
```

## Usage

To run the service:

```bash
(.venv) $ uvicorn main:app --reload
```

You can open it in the browser or query it from the command line:

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
