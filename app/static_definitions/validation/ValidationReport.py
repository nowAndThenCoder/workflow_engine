from dataclasses import dataclass, field
from typing import List


@dataclass
class ValidationReport:
    is_valid: bool = True
    errors: List[str] = field(default_factory=list)

    def add_error(self, message: str):
        self.is_valid = False
        self.errors.append(message)

    def merge(self, other: "ValidationReport"):
        if not other.is_valid:
            self.is_valid = False
            self.errors.extend(other.errors)
