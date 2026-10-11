from dataclasses import dataclass

from .enums.ApplicationType import ApplicationType
from .base.application.FunctionalApplicationDefinition import FunctionalApplicationDefinition

@dataclass
class UserInteractionApplicationDefinition(FunctionalApplicationDefinition):
    
    def __init__(self, name: str, script_content: str):
        super().__init__(name, ApplicationType.USER_INTERACTION, script_content)
