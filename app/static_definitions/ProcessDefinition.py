from dataclasses import dataclass, field
from typing import List

from .base.AbstractDefinition import AbstractDefinition
from .base.event.AbstractEventDefinition import AbstractEventDefinition
from .base.node.AbstractNodeDefinition import AbstractNodeDefinition
from .GatewayDefinition import GatewayDefinition
from .enums.GatewayDirection import GatewayDirection
from .enums.GatewayLogic import GatewayLogic
from .TaskDefinition import TaskDefinition
from .TransitionDefinition import TransitionDefinition
from .FormalParameterDefinition import FormalParameterDefinition

from .validation.ValidationReport import ValidationReport

@dataclass
class ProcessDefinition(AbstractDefinition):

    nodes:             List[AbstractNodeDefinition]    = field(default_factory=list)
    events:            List[AbstractEventDefinition]   = field(default_factory=list)
    tasks:             List[TaskDefinition]            = field(default_factory=list)
    transitions:       List[TransitionDefinition]      = field(default_factory=list)
    formal_parameters: List[FormalParameterDefinition] = field(default_factory=list)

    def __init__(self, name: str):
        super().__init__(name)
        self.nodes = []
        self.events = []
        self.tasks = []
        self.transitions = []
        self.formal_parameters = []
    
    def add_transition(self, source: AbstractNodeDefinition, target: AbstractNodeDefinition, index: int = 0):
        for t in self.transitions:
            if t.source == source and t.index == index:
                raise ValueError(f"Knoten hat bereits eine Transition mit sort_index {index}.")

        new_t = TransitionDefinition(
            source=source,
            target=target,
            index=index
        )
        
        self.transitions.append(new_t)
