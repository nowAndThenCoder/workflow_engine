from dataclasses import dataclass, field
from typing import Optional


from .base.AbstractDefinition import AbstractDefinition
from .enums.ParameterDirection import ParameterDirection
from .VariableTypeDefinition import VariableTypeDefinition

@dataclass
class FormalParameterDefinition(AbstractDefinition):
    
    variable_type:  Optional[VariableTypeDefinition]    = field(default=None)
    direction:      Optional[ParameterDirection]        = field(default=None)
        
    def __init__(self, name: str, variable_type: VariableTypeDefinition, direction: ParameterDirection):
        super().__init__(name)
        self.variable_type = variable_type
        self.direction = direction
