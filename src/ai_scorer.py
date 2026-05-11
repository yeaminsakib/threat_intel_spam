"""Spam scoring helpers and model-loading utilities."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import joblib
except ImportError:  # pragma: no cover - optional dependency for the scaffold
    joblib = None


@dataclass
class SpamScorer:
    """Thin wrapper around a persisted spam classifier."""

    model_path: Path
    model: Any | None = None

    def load(self) -> Any | None:
        """Load the serialized model if it exists."""

        if self.model is not None:
            return self.model

        if joblib is None or not self.model_path.exists():
            return None

        self.model = joblib.load(self.model_path)
        return self.model

    def score(self, features: list[float]) -> float:
        """Return a spam probability or a conservative fallback score."""

        model = self.load()
        if model is not None and hasattr(model, "predict_proba"):
            probability = model.predict_proba([features])[0]
            return float(probability[-1])

        return 0.0
