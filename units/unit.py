from dataclasses import dataclass
from typing import Dict

from units.util import canonicalize_symbol


@dataclass(eq=False)
class Unit:
    __slots__ = ['symbol', 'dimension']
    symbol: str
    dimension: Dict[str, int]

    def __post_init__(self):
        self.validate()
        self.symbol = canonicalize_symbol(self.symbol)

    def __eq__(self, other):
        if not isinstance(other, Unit):
            raise TypeError(f"Unsupported operand type: {type(other)}")
        return self.symbol == other.symbol and self.dimension == other.dimension

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        if not isinstance(other, Unit):
            raise TypeError(f"Unsupported operand type: {type(other)}")
        new_dimension = self.dimension.copy()
        for dim, power in other.dimension.items():
            new_dimension[dim] = new_dimension.get(dim, 0) + power
        new_symbol = f"{self.symbol}*{other.symbol}"
        result = Unit(canonicalize_symbol(new_symbol), new_dimension)
        result.remove_zero_dimensions()
        return result

    def __truediv__(self, other):
        if not isinstance(other, Unit):
            raise TypeError(f"Unsupported operand type: {type(other)}")
        new_dimension = self.dimension.copy()
        for dim, power in other.dimension.items():
            new_dimension[dim] = new_dimension.get(dim, 0) - power
        new_symbol = f"{self.symbol}/{other.symbol}"
        result = Unit(canonicalize_symbol(new_symbol), new_dimension)
        result.remove_zero_dimensions()
        return result

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError(f"Exponent must be an integer: {type(power)}")
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
        dimension_str = ', '.join(f"{dim}^{power}" if power != 1 else dim for dim, power in self.dimension.items())
        return f"{self.symbol} ({dimension_str})"

    def validate(self):
        if not all(isinstance(val, int) for val in self.dimension.values()):
            raise ValueError("All dimension powers must be integers")

    def remove_zero_dimensions(self):
        # Remove dimensions with a power of 0
        self.dimension = {k: v for k, v in self.dimension.items() if v != 0}

        if not self.dimension:
            self.symbol = ""