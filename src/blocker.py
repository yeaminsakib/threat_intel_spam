"""Blocking rule generation for suspicious senders and indicators."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BlockRule:
    """A simple block rule for a single indicator."""

    indicator_type: str
    value: str
    reason: str = "suspicious activity"


def build_block_rules(iocs: dict[str, set[str]]) -> list[BlockRule]:
    """Convert extracted indicators into block rules."""

    rules: list[BlockRule] = []
    for indicator_type, values in iocs.items():
        for value in sorted(values):
            rules.append(BlockRule(indicator_type=indicator_type, value=value))
    return rules
