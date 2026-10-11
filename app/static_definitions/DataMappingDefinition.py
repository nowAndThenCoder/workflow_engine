from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

from .base.AbstractDefinition import AbstractDefinition
from .FormalParameterDefinition import FormalParameterDefinition
from .VariableDefinition import VariableDefinition

if TYPE_CHECKING:
    from .TaskDefinition import TaskDefinition


@dataclass
class DataMappingDefinition(AbstractDefinition):
    
    formal_parameter:   Optional[FormalParameterDefinition] = field(default=None)
    variable:           Optional[VariableDefinition]        = field(default=None)    
    task:               Optional["TaskDefinition"]          = field(default=None)   

    def __init__(self, name: str, formal_parameter: FormalParameterDefinition, variable: VariableDefinition):
        super().__init__(name)
        self.formal_parameter = formal_parameter
        self.variable = variable

    def set_task(self, task: "TaskDefinition") -> None:
        self.task = task