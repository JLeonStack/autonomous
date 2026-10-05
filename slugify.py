"""A dependency-free ASCII slug utility."""

import re

_SEPARATORS = re.compile(r"[^A-Za-z0-9]+")


def slugify(text: str) -> str:
    # Substitute before lowercasing: some non-ASCII characters (e.g. the
    # Kelvin sign U+212A) lowercase to an ASCII letter, which would wrongly
    # stop them from being treated as separators.
    return _SEPARATORS.sub("-", text).lower().strip("-")
