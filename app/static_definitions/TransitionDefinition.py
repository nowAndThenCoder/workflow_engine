
import ast
from dataclasses import dataclass

from .base.node.AbstractNodeDefinition import AbstractNodeDefinition
from .validation.ValidationReport import ValidationReport
    

@dataclass
class TransitionDefinition:
    
    source: AbstractNodeDefinition
    target: AbstractNodeDefinition
    index:  int
    condition_expression: str

    def __init__(self, source: AbstractNodeDefinition, target: AbstractNodeDefinition, index: int, condition: str = "True"):
        super().__init__()
        self.source = source
        self.target = target
        self.index = index
        self.condition_expression = condition

    def validate_condition_expression(self, expression: str, report: ValidationReport, transition_name: str):
        try:
            # Parsen des Ausdrucks
            tree = ast.parse(expression, mode="eval")

            # Prüfung: Es darf nur eine "Expression" sein (keine Statements, keine Funktions-Definitionen)
            if not isinstance(tree, ast.Expression):
                report.add_error(
                    f"Transition '{transition_name}': Must be a simple expression, not a code block."
                )
                return

            # Tiefenprüfung: Verbot von Funktionsaufrufen oder komplexen Logiken (optional, je nach Strenge)
            for node in ast.walk(tree):
                if isinstance(
                    node,
                    (
                        ast.FunctionDef,
                        ast.AsyncFunctionDef,
                        ast.ClassDef,
                        ast.Import,
                        ast.ImportFrom,
                    ),
                ):
                    report.add_error(
                        f"Transition '{transition_name}': Forbidden syntax (e.g., 'def', 'class', 'import') found."
                    )

                # Optional: Aufrufe verbieten, wenn nur Variablen-Vergleiche erlaubt sein sollen
                # if isinstance(node, ast.Call):
                #     report.add_error(f"Transition '{transition_name}': Function calls are not allowed in expressions.")

        except SyntaxError as e:
            report.add_error(
                f"Transition '{transition_name}': Invalid Python syntax: {str(e)}"
            )
