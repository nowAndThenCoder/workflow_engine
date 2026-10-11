from dataclasses import dataclass, field
from typing import List, Optional

from .base.AbstractDefinition import AbstractDefinition
from .enums.VariableBaseTypes import VariableBaseTypes


@dataclass
class VariableTypeDefinition(AbstractDefinition):

    child_elements:     List["VariableTypeDefinition"] = field(default_factory=list)
    variable_base_type: Optional[VariableBaseTypes]    = field(default=None)

    def __init__(self, name: str, variable_base_type: VariableBaseTypes):
        super().__init__(name)
        self.child_elements = []
        self.variable_base_type = variable_base_type
