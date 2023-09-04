# Base Units
from units.unit import Unit

METER = Unit("m", {"Length": 1})
SECOND = Unit("s", {"Time": 1})
KILOGRAM = Unit("kg", {"Mass": 1})

# Derived Units
VELOCITY = METER / SECOND  # m/s
ACCELERATION = VELOCITY / SECOND  # m/s^2
FORCE = KILOGRAM * ACCELERATION  # kg*m/s^2, Newton

# Constants
GRAVITY = Unit("g", {"Length": 1, "Time": -2})  # m/s^2, gravitational acceleration
SPEED_OF_LIGHT = Unit("c", {"Length": 1, "Time": -1})  # m/s
