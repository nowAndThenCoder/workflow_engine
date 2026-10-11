from dataclasses import dataclass
import uuid


@dataclass
class AbstractNodeDefinition:

    id: str

    def __init__(self):
        self.id = str(uuid.uuid4())
