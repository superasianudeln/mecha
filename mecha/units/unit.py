class Unit:
    def __init__(self, dimension):
        self.dimension = dimension
        self.unit = self.compute_unit()

    def compute_unit(self):
        base_units = {'M': 'kg', 'L': 'm', 'T': 's'}

        # Generate a list of tuples containing the base unit and its power
        unit_parts = [(base_units[dim], power) for dim, power in self.dimension.items() if power != 0]

        # Sort the list of tuples based on the base unit and then by power
        sorted_unit_parts = sorted(unit_parts, key=lambda x: (x[0], x[1]))

        # Convert the sorted list of tuples to a list of strings
        sorted_unit_strings = [f"{unit}^{power}" if power != 1 else unit for unit, power in sorted_unit_parts]

        # Join the sorted list of strings to form the final unit string
        return '*'.join(sorted_unit_strings)

    def __add__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions must be identical for addition or subtraction.")
        # Since dimensions are the same, we can return either unit
        return Unit(self.dimension)

    def __sub__(self, other):
        return self.__add__(other)  # Addition and subtraction have the same requirement

    def __mul__(self, other):
        new_dimension = {}
        for dim in set(self.dimension) | set(other.dimension):
            new_dimension[dim] = self.dimension.get(dim, 0) + other.dimension.get(dim, 0)
        return Unit(new_dimension)

    def __truediv__(self, other):
        new_dimension = {}
        for dim in set(self.dimension) | set(other.dimension):
            new_dimension[dim] = self.dimension.get(dim, 0) - other.dimension.get(dim, 0)
        return Unit(new_dimension)

    def __pow__(self, power):
        new_dimension = {dim: val * power for dim, val in self.dimension.items()}
        return Unit(new_dimension)

    def __eq__(self, other):
        return self.dimension == other.dimension

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return str(self) < str(other)

    def __le__(self, other):
        return str(self) <= str(other)

    def __gt__(self, other):
        return str(self) > str(other)

    def __ge__(self, other):
        return str(self) >= str(other)

    def __str__(self):
        return self.unit
