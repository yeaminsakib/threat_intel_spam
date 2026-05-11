"""Utilities for extracting and normalizing email headers."""
from __future__ import annotations

from email import policy
from email.parser import BytesParser
from pathlib import Path


def parse_headers(eml_path: Path) -> dict[str, str]:
    """Return a normalized header dictionary for a raw .eml file."""

    with eml_path.open("rb") as handle:
        message = BytesParser(policy=policy.default).parse(handle)

    headers: dict[str, str] = {}
    for key, value in message.items():
        headers[key.lower()] = str(value)

    return headers
