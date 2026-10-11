from dataclasses import dataclass


@dataclass
class AbstractDefinition:

    name: str

    def __init__(self, name: str):
        self.name = name
