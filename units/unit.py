from typing import Dict
from dataclasses import dataclass, field
from units.util import canonicalize_symbol


@dataclass(eq=False)
class Unit:
    symbol: str
    dimension: Dict[str, int]

    def __post_init__(self):
        self.validate()
        self.symbol = canonicalize_symbol(self.symbol)

    def __eq__(self, other):
        return self.symbol == other.symbol and self.dimension == other.dimension

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        new_dimension = self.dimension.copy()
        for dim, power in other.dimension.items():
            new_dimension[dim] = new_dimension.get(dim, 0) + power
        new_symbol = f"{self.symbol}*{other.symbol}"
        result = Unit(canonicalize_symbol(new_symbol), new_dimension)
        result.remove_zero_dimensions()
        return result

    def __truediv__(self, other):
        new_dimension = self.dimension.copy()
        for dim, power in other.dimension.items():
            new_dimension[dim] = new_dimension.get(dim, 0) - power
        new_symbol = f"{self.symbol}/{other.symbol}"
        result = Unit(canonicalize_symbol(new_symbol), new_dimension)
        result.remove_zero_dimensions()
        return result

    def __pow__(self, power):
        new_dimension = {dim: power * val for dim, val in self.dimension.items()}
        # Check if the symbol is a compound unit
        if '*' in self.symbol or '/' in self.symbol:
            new_symbol = f"({self.symbol})^{power}"
        else:
            new_symbol = f"{self.symbol}^{power}"
        result = Unit(canonicalize_symbol(new_symbol), new_dimension)
        result.remove_zero_dimensions()
        return result

    def __str__(self):
        return f"{self.symbol} ({self.dimension})"

    def validate(self):
        if not all(isinstance(val, int) for val in self.dimension.values()):
            raise ValueError("All dimension powers must be integers")

    def remove_zero_dimensions(self):
        # Remove dimensions with a power of 0
        self.dimension = {k: v for k, v in self.dimension.items() if v != 0}

        if not self.dimension:
            self.symbol = ""


# Base Units
Unit.METER = Unit("m", {"length": 1})
Unit.SECOND = Unit("s", {"time": 1})
Unit.KILOGRAM = Unit("kg", {"mass": 1})

# Derived Units
Unit.VELOCITY = Unit.METER / Unit.SECOND  # m/s
Unit.ACCELERATION = Unit.VELOCITY / Unit.SECOND  # m/s^2
Unit.FORCE = Unit.KILOGRAM * Unit.ACCELERATION  # kg*m/s^2, Newton

# Constants
Unit.GRAVITY = Unit("g", {"length": 1, "time": -2})  # m/s^2, gravitational acceleration
Unit.SPEED_OF_LIGHT = Unit("c", {"length": 1, "time": -1})  # m/s
