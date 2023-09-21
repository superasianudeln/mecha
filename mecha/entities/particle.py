from typing import Type, Union

from mecha.maths.vector import Vector
from mecha.units.constants import ACCELERATION_UNIT, KILOGRAM, VELOCITY_UNIT
from mecha.units.physical_quantity import PhysicalQuantity
from mecha.units.unit import Unit


def _initialize_property(value: Union[Type[PhysicalQuantity], float, Vector], unit: Unit) -> PhysicalQuantity:
    if isinstance(value, PhysicalQuantity):
        return value
    return PhysicalQuantity(value, unit)


class Particle:
    def __init__(
        self,
        position: Vector,
        mass: float = 1.0,
        velocity: Union[Type[PhysicalQuantity], float, Vector] = 0.0,
        acceleration: Union[Type[PhysicalQuantity], float, Vector] = 0.0,
    ):
        self._position = position
        self._mass = PhysicalQuantity(mass, KILOGRAM)
        self._velocity = _initialize_property(velocity, VELOCITY_UNIT)
        self._acceleration = _initialize_property(acceleration, ACCELERATION_UNIT)

    @property
    def position(self) -> Vector:
        return self._position

    @position.setter
    def position(self, value: Vector):
        self._position = value

    @property
    def velocity(self) -> PhysicalQuantity:
        return self._velocity

    @velocity.setter
    def velocity(self, value: PhysicalQuantity):
        self._velocity = value

    @property
    def acceleration(self) -> PhysicalQuantity:
        return self._acceleration

    @acceleration.setter
    def acceleration(self, value: PhysicalQuantity):
        self._acceleration = value

    @property
    def mass(self) -> PhysicalQuantity:
        return self._mass

    @mass.setter
    def mass(self, value: PhysicalQuantity):
        self._mass = value

    def __str__(self) -> str:
        return (
            f"Particle(position={self.position}, velocity={self.velocity}, "
            f"acceleration={self.acceleration}, mass={self.mass})"
        )

    def __repr__(self) -> str:
        return (
            f"Particle(position={self.position!r}, velocity={self.velocity!r}, "
            f"acceleration={self.acceleration!r}, mass={self.mass!r})"
        )
