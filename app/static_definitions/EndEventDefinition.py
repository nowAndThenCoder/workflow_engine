from dataclasses import dataclass

from .base.event.AbstractEventDefinition import AbstractEventDefinition
from .enums.EventTypes import EventTypes


@dataclass
class EndEventDefinition(AbstractEventDefinition):

    def __init__(self):
        super().__init__(EventTypes.END)
