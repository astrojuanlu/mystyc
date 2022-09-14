from __future__ import annotations

import typing as t

from rst_to_myst import rst_to_myst


def convert(input_rest: str) -> dict[str, str]:
    output = rst_to_myst(
        input_rest,
        use_sphinx=False,
    )
    return {"input_rest": input_rest, "output_myst": output.text}
