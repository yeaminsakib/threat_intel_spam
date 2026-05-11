"""IOC extraction helpers for IPs, domains, URLs, and hashes."""
from __future__ import annotations

import re
from collections.abc import Iterable

IP_PATTERN = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b")
DOMAIN_PATTERN = re.compile(r"\b(?:[a-z0-9-]+\.)+[a-z]{2,}\b", re.IGNORECASE)
URL_PATTERN = re.compile(r"https?://[^\s'\"]+", re.IGNORECASE)
MD5_PATTERN = re.compile(r"\b[a-fA-F0-9]{32}\b")
SHA1_PATTERN = re.compile(r"\b[a-fA-F0-9]{40}\b")
SHA256_PATTERN = re.compile(r"\b[a-fA-F0-9]{64}\b")


def extract_iocs(text: str) -> dict[str, set[str]]:
    """Extract a small set of common indicators from free-form text."""

    return {
        "ips": set(IP_PATTERN.findall(text)),
        "domains": set(DOMAIN_PATTERN.findall(text)),
        "urls": set(URL_PATTERN.findall(text)),
        "md5": set(MD5_PATTERN.findall(text)),
        "sha1": set(SHA1_PATTERN.findall(text)),
        "sha256": set(SHA256_PATTERN.findall(text)),
    }
