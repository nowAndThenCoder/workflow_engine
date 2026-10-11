from dataclasses import dataclass, field
from typing import List, Optional, TYPE_CHECKING

from .base.AbstractDefinition import AbstractDefinition
from .base.application.AbstractApplicationDefinition import AbstractApplicationDefinition
from .base.node.AbstractNodeDefinition import AbstractNodeDefinition
from .DataMappingDefinition import DataMappingDefinition
from .FormalParameterDefinition import FormalParameterDefinition

if TYPE_CHECKING:
    from .DataMappingDefinition import DataMappingDefinition

@dataclass
class TaskDefinition(AbstractDefinition, AbstractNodeDefinition):

    formal_parameters: List[FormalParameterDefinition]          = field(default_factory=list)
    data_mappings:     List[DataMappingDefinition]              = field(default_factory=list)
    application:       Optional[AbstractApplicationDefinition]  = field(default=None)

    def __init__(self, name: str, application: AbstractApplicationDefinition):
        super().__init__(name)
        self.application = application
