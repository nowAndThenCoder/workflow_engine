from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from typing import List

from .AbstractApplicationDefinition import AbstractApplicationDefinition

if TYPE_CHECKING:
    from ...enums.ApplicationType import ApplicationType
    from ...FormalParameterDefinition import FormalParameterDefinition

@dataclass
class FunctionalApplicationDefinition(AbstractApplicationDefinition):
    
    formal_parameters:  List["FormalParameterDefinition"]   = field(default_factory=list)    
    script_content:     Optional[str]                       = field(default=None)

    def __init__(self, name: str, app_type: "ApplicationType", script_content: Optional[str] = None):
        super().__init__(name, app_type)
        self.script_content = script_content
        self.formal_parameters = []