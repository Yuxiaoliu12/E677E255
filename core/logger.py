"""ML-friendly search logging.

Logs decision points as JSONL records for training data generation.
Each record captures the state, the choice made, and the outcome.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, TextIO

import numpy as np


@dataclass
class DecisionRecord:
    """One logged decision point during search."""

    step: int
    n: int
    num_assigned: int
    chosen_cell: tuple[int, int]
    chosen_value: int
    available_values: list[int]
    propagation_count: int = 0
    features: dict[str, float] = field(default_factory=dict)
    # Filled in after resolution
    outcome: str = ""  # 'success', 'dead_end', 'pruned', 'backtrack'
    depth_to_contradiction: int | None = None
    contradiction_reason: str = ""


class SearchLogger:
    """Streams decision records to a JSONL file."""

    def __init__(self, path: Path | str | None = None):
        self.path = Path(path) if path else None
        self._file: TextIO | None = None
        self._records: list[DecisionRecord] = []
        self.enabled = path is not None

    def open(self) -> None:
        if self.path:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self._file = open(self.path, "a")

    def close(self) -> None:
        if self._file:
            self._file.close()
            self._file = None

    def log_decision(self, record: DecisionRecord) -> None:
        self._records.append(record)
        if self._file:
            self._file.write(json.dumps(asdict(record)) + "\n")
            self._file.flush()

    def log_contradiction(
        self, step: int, n: int, reason: str, num_assigned: int
    ) -> None:
        if self._file:
            entry = {
                "type": "contradiction",
                "step": step,
                "n": n,
                "reason": reason,
                "num_assigned": num_assigned,
                "timestamp": time.time(),
            }
            self._file.write(json.dumps(entry) + "\n")
            self._file.flush()

    def log_model_found(self, step: int, n: int, table: np.ndarray) -> None:
        if self._file:
            entry = {
                "type": "model_found",
                "step": step,
                "n": n,
                "table": table.tolist(),
                "timestamp": time.time(),
            }
            self._file.write(json.dumps(entry) + "\n")
            self._file.flush()

    @property
    def records(self) -> list[DecisionRecord]:
        return self._records

    def __enter__(self) -> SearchLogger:
        self.open()
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()


class NullLogger(SearchLogger):
    """No-op logger for when logging is disabled."""

    def __init__(self) -> None:
        super().__init__(path=None)
        self.enabled = False

    def log_decision(self, record: DecisionRecord) -> None:
        pass

    def log_contradiction(self, *args: Any, **kwargs: Any) -> None:
        pass

    def log_model_found(self, *args: Any, **kwargs: Any) -> None:
        pass
