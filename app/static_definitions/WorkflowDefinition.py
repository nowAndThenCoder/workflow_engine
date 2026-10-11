
from dataclasses import dataclass, field
from typing import List

from .base.AbstractDefinition import AbstractDefinition
from .base.application.AbstractApplicationDefinition import AbstractApplicationDefinition
from .ProcessDefinition import ProcessDefinition
from .VariableDefinition import VariableDefinition
from .VariableTypeDefinition import VariableTypeDefinition


@dataclass
class WorkflowDefinition(AbstractDefinition):

    processes:      List[ProcessDefinition]                 = field(default_factory=list)
    variable_types: List[VariableTypeDefinition]            = field(default_factory=list)
    variables:      List[VariableDefinition]                = field(default_factory=list)
    applications:   List[AbstractApplicationDefinition]     = field(default_factory=list)

    def __init__(self, name: str):
        super().__init__(name)
        self.processes = []
        self.variable_types = []
        self.variables = []
        self.applications = []
