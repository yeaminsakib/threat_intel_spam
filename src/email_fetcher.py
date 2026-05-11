"""IMAP email collection helpers for threat intel ingestion."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class EmailFetchConfig:
    """Connection settings for an IMAP mailbox."""

    host: str
    username: str
    password: str
    mailbox: str = "INBOX"
    ssl: bool = True


def fetch_emails(config: EmailFetchConfig, limit: int | None = None) -> list[bytes]:
    """Fetch raw email messages from an IMAP mailbox.

    This scaffold keeps the collection logic isolated so the project can grow
    into a real collector without changing the public API.
    """

    raise NotImplementedError("IMAP collection is not implemented yet.")


def save_raw_emails(messages: Iterable[bytes], output_dir: Path) -> list[Path]:
    """Persist raw .eml payloads to disk."""

    output_dir.mkdir(parents=True, exist_ok=True)
    saved_paths: list[Path] = []

    for index, message in enumerate(messages, start=1):
        path = output_dir / f"email_{index:05d}.eml"
        path.write_bytes(message)
        saved_paths.append(path)

    return saved_paths
