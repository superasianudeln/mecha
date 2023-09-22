import numpy as np


class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.vector = np.array([x, y, z])

    @property
    def magnitude(self) -> np.float64:
        return np.linalg.norm(self.vector)

    @property
    def direction(self) -> np.ndarray:
        if self.magnitude == 0:
            error_msg = "Zero vector does not have a direction"
            raise ValueError(error_msg)
        return self.vector / self.magnitude

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(*self.vector + other.vector)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(*self.vector - other.vector)

    def dot(self, other: "Vector") -> float:
        return np.dot(self.vector, other.vector)

    def cross(self, other: "Vector") -> "Vector":
        x1, y1, z1 = self.vector
        x2, y2, z2 = other.vector
        return Vector(y1 * z2 - y2 * z1, z1 * x2 - z2 * x1, x1 * y2 - x2 * y1)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(*(self.vector * scalar))

    def __truediv__(self, scalar: float) -> "Vector":
        if scalar == 0:
            msg = "Cannot divide by zero"
            raise ValueError(msg)
        return Vector(*(self.vector / scalar))

    def __str__(self) -> str:
        return str(self.vector)

    def __repr__(self) -> str:
        return f"Vector{tuple(self.vector)}"

    def __eq__(self, other: "Vector") -> bool:
        return np.array_equal(self.vector, other.vector)

    def __len__(self) -> int:
        return len(self.vector)
