from dataclasses import dataclass

from .base.application.AbstractApplicationDefinition import AbstractApplicationDefinition
from .enums.ApplicationType import ApplicationType


@dataclass
class NoneApplicationDefinition(AbstractApplicationDefinition):

    def __init__(self, name: str):
        super().__init__(name, ApplicationType.NONE)
