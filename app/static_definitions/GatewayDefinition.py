from dataclasses import dataclass

from .base.node.AbstractNodeDefinition import AbstractNodeDefinition
from .enums.GatewayDirection import GatewayDirection
from .enums.GatewayLogic import GatewayLogic

@dataclass
class GatewayDefinition(AbstractNodeDefinition):
    logic:      GatewayLogic
    direction:  GatewayDirection

    def __init__(self, logic: GatewayLogic, direction: GatewayDirection):
        super().__init__()
        self.logic = logic
        self.direction = direction
