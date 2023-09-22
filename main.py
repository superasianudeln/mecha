from mecha.maths.vector import Vector
from mecha.units.constants import METER
from mecha.units.physical_quantity import PhysicalQuantity

x = PhysicalQuantity(1, METER)

y = PhysicalQuantity(Vector(1, 2, 3), METER)

print(x + y)
