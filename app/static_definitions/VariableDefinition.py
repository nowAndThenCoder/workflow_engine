from dataclasses import dataclass, field
from typing import Optional

from .base.AbstractDefinition import AbstractDefinition
from .VariableTypeDefinition import VariableTypeDefinition


@dataclass
class VariableDefinition(AbstractDefinition):

    variable_type: Optional[VariableTypeDefinition] = field(default=None)

    def __init__(self,name: str,variable_type: VariableTypeDefinition):
        super().__init__(name)
        self.variable_type = variable_type
