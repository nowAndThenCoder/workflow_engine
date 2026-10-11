from dataclasses import dataclass

import enum
from typing import Any, Type
from datetime import date, datetime

@dataclass(frozen=True)
class VariableType:
    name: str
    python_type: Type
    default_value: Any

class VariableBaseTypes(enum.Enum):
    STRING = VariableType("String", str, "")
    DATE = VariableType("DATE", date, date.today)
    DATETIME = VariableType("DATETIME", datetime, datetime.now)
    INTEGER = VariableType("Integer", int, 0)
    FLOAT = VariableType("Float", float, 0.0)
    BOOLEAN = VariableType("Boolean", bool, False)
    STRUCTURED = VariableType("STRUCTURED", object, None)