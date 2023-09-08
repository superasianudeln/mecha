from mecha.entities.particle import Particle
from mecha.maths.vector import Vector
from mecha.units.physical_quantity import PhysicalQuantity
from mecha.units.constants import KILOGRAM, VELOCITY_UNIT, ACCELERATION_UNIT

position_vector = Vector(1.0, 2.0, 3.0)  # Example values for x, y, z coordinates
a = PhysicalQuantity(position_vector, VELOCITY_UNIT)

particle = Particle(mass=1, position=position_vector, velocity=position_vector, acceleration=position_vector)
print(particle)

particle.mass = particle.mass * 2
print(a)
print(particle.velocity)
particle.velocity = particle.velocity + a

print(particle)
