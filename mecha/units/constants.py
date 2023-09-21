# Base Units
from mecha.units.unit import Unit

METER = Unit({"L": 1})
SECOND = Unit({"T": 1})
KILOGRAM = Unit({"M": 1})

# Derived Units
VELOCITY_UNIT = METER / SECOND  # m/s
ACCELERATION_UNIT = VELOCITY_UNIT / SECOND  # m/s^2
FORCE_UNIT = Unit({"M": 1, "L": 1, "T": -2})  # kg*m/s^2, Newton

SQ_METER = Unit({"M": 2})
