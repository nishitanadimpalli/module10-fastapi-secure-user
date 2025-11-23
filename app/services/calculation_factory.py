from abc import ABC, abstractmethod
from app.models import CalculationType


class CalculationOperation(ABC):
    @abstractmethod
    def compute(self, a: float, b: float) -> float:
        ...


class AddOperation(CalculationOperation):
    def compute(self, a, b):
        return a + b


class SubOperation(CalculationOperation):
    def compute(self, a, b):
        return a - b


class MultiplyOperation(CalculationOperation):
    def compute(self, a, b):
        return a * b


class DivideOperation(CalculationOperation):
    def compute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


class CalculationFactory:
    @staticmethod
    def get_operation(calc_type: CalculationType):
        if calc_type == CalculationType.ADD:
            return AddOperation()
        if calc_type == CalculationType.SUB:
            return SubOperation()
        if calc_type == CalculationType.MULTIPLY:
            return MultiplyOperation()
        if calc_type == CalculationType.DIVIDE:
            return DivideOperation()

        raise ValueError("Invalid operation type")
