from typing import Union

from mecha.maths.vector import Vector
from mecha.units.unit import Unit


class PhysicalQuantity:
    def __init__(self, value: Union[float, Vector], unit: Unit):
        self.value = value
        self.unit = unit

    def _check_units(self, other: 'PhysicalQuantity') -> None:
        if self.unit != other.unit:
            raise ValueError(
                f"Incompatible units: {self.unit} and {other.unit} cannot be used together in this operation.")

    def __add__(self, other: 'PhysicalQuantity') -> 'PhysicalQuantity':
        self._check_units(other)
        return PhysicalQuantity(self.value + other.value, self.unit)

    def __sub__(self, other: 'PhysicalQuantity') -> 'PhysicalQuantity':
        self._check_units(other)
        return PhysicalQuantity(self.value - other.value, self.unit)

    def __mul__(self, other: Union['PhysicalQuantity', float, int]) -> 'PhysicalQuantity':
        if isinstance(other, PhysicalQuantity):
            return PhysicalQuantity(self.value * other.value, self.unit * other.unit)
        elif isinstance(other, (float, int)):
            return PhysicalQuantity(self.value * other, self.unit)
        else:
            raise ValueError(f"Unsupported type {type(other)} for multiplication with PhysicalQuantity.")

    def __rmul__(self, other):  # This method handles multiplication when the scalar is on the left
        return self.__mul__(other)

    def __truediv__(self, other: Union['PhysicalQuantity', float, int]) -> 'PhysicalQuantity':
        if isinstance(other, (float, int)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return PhysicalQuantity(self.value / other, self.unit)
        elif isinstance(other, PhysicalQuantity):
            if other.value == 0:
                raise ValueError("Cannot divide by zero")
            return PhysicalQuantity(self.value / other.value, self.unit / other.unit)
        else:
            raise ValueError(f"Unsupported type {type(other)} for division with PhysicalQuantity.")

    def __pow__(self, power: float) -> 'PhysicalQuantity':
        if isinstance(self.value, Vector):
            # Raising a vector to a power using its magnitude
            magnitude_power = self.value.magnitude ** power
            return PhysicalQuantity(magnitude_power, self.unit ** power)
        else:
            return PhysicalQuantity(self.value ** power, self.unit ** power)

    def __eq__(self, other):
        return self.value == other.value and self.unit == other.unit

    def __str__(self) -> str:
        return f"{self.value} {self.unit.unit}"

    def __repr__(self) -> str:
        return f"PhysicalQuantity(value={self.value}, unit={self.unit})"
