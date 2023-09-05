from mecha.maths.vector import Vector
from mecha.units.constants import *
from mecha.units.physical_quantity import PhysicalQuantity


class Particle:
    def __init__(self, position: Vector, mass: float = 1.0, velocity: float = 0.0, acceleration: float = 0.0):
        self._position = position
        self._mass = PhysicalQuantity(mass, KILOGRAM)
        self._velocity = PhysicalQuantity(velocity, VELOCITY_UNIT)
        self._acceleration = PhysicalQuantity(acceleration, ACCELERATION_UNIT)

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
        return (f"Particle(position={self.position}, velocity={self.velocity}, "
                f"acceleration={self.acceleration}, mass={self.mass})")

    __repr__ = __str__
