from dataclasses import dataclass

from ...enums.EventTypes import EventTypes
from ..node.AbstractNodeDefinition import AbstractNodeDefinition


@dataclass
class AbstractEventDefinition(AbstractNodeDefinition):

    event_type: EventTypes

    def __init__(self, event_type: EventTypes):
        super().__init__()
        self.event_type = event_type
