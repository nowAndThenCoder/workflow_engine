from dataclasses import dataclass

from ...enums.ApplicationType import ApplicationType
from ..AbstractDefinition import AbstractDefinition


@dataclass
class AbstractApplicationDefinition(AbstractDefinition):

    app_type: ApplicationType

    def __init__(self, name: str, app_type: ApplicationType):
        super().__init__(name)
        self.app_type = app_type
