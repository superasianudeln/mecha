import inspect
from typing import NoReturn, Union

from mecha.maths.vector import Vector
from mecha.units.unit import Unit


class PhysicalQuantity:
    def __init__(self, value: Union[float, Vector], unit: Unit):
        self._value = value
        self._unit = unit

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    def _check_units(self, other: "PhysicalQuantity") -> None:
        if self.unit != other.unit:
            msg = f"Incompatible units: {self.unit} and {other.unit} cannot be used together in this operation."
            raise ValueError(msg)

    def _raise_unsupported_type_error(self) -> NoReturn:
        frame = inspect.currentframe()

        if frame is not None and frame.f_back is not None:
            current_function_name = frame.f_back.f_code.co_name
        else:
            current_function_name = "Unknown"

        current_class_name = self.__class__.__name__

        msg = (
            f"Error in {current_class_name}.{current_function_name}: Unsupported operand type encountered. "
            f"ensure that the operands are compatible with the '{current_class_name}'class and the '{current_function_name}' method."
        )
        raise ValueError(msg)

    def __add__(self, other: "PhysicalQuantity") -> "PhysicalQuantity":
        self._check_units(other)

        if isinstance(self.value, Vector) and isinstance(other.value, Vector):
            return PhysicalQuantity(self.value + other.value, self.unit)

        if isinstance(self.value, (float, int)) and isinstance(other.value, (float, int)):
            return PhysicalQuantity(self.value + other.value, self.unit)

        return self._raise_unsupported_type_error()

    def __sub__(self, other: "PhysicalQuantity") -> "PhysicalQuantity":
        self._check_units(other)
        if isinstance(self.value, Vector) and isinstance(other.value, Vector):
            return PhysicalQuantity(self.value - other.value, self.unit)
        if isinstance(self.value, (float, int)) and isinstance(other.value, (float, int)):
            return PhysicalQuantity(self.value - other.value, self.unit)
        return self._raise_unsupported_type_error()

    def __mul__(self, other: Union["PhysicalQuantity", float]) -> "PhysicalQuantity":
        if isinstance(other, PhysicalQuantity):
            return PhysicalQuantity(self.value * other.value, self.unit * other.unit)
        elif isinstance(other, (float, int)):
            return PhysicalQuantity(self.value * other, self.unit)
        else:
            msg = f"Unsupported type {type(other)} for multiplication with PhysicalQuantity."
            raise ValueError(msg)

    def __rmul__(self, other):  # This method handles multiplication when the scalar is on the left
        return self.__mul__(other)

    def __truediv__(self, other: Union["PhysicalQuantity", float]) -> "PhysicalQuantity":
        if isinstance(other, (float, int)):
            if other == 0:
                msg = "Cannot divide by zero"
                raise ValueError(msg)
            return PhysicalQuantity(self.value / other, self.unit)
        if isinstance(other, PhysicalQuantity):
            if other.value == 0:
                msg = "Cannot divide by zero"
                raise ValueError(msg)
            return PhysicalQuantity(self.value / other.value, self.unit / other.unit)
        msg = f"Unsupported type {type(other)} for division with PhysicalQuantity."
        raise ValueError(msg)

    def __pow__(self, power: float) -> "PhysicalQuantity":
        if isinstance(self.value, Vector):
            # Raising a vector to a power using its magnitude
            magnitude_power = self.value.magnitude**power
            return PhysicalQuantity(magnitude_power, self.unit**power)
        else:
            return PhysicalQuantity(self.value**power, self.unit**power)

    def __eq__(self, other: "PhysicalQuantity") -> bool:
        return self.value == other.value and self.unit == other.unit

    def __neg__(self) -> "PhysicalQuantity":
        return PhysicalQuantity(-self.value, self.unit)

    def __str__(self) -> str:
        return f"{self.value} {self.unit.unit}"

    def __repr__(self) -> str:
        return f"PhysicalQuantity(value={self.value}, unit={self.unit})"
