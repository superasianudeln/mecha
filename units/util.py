import re
from collections import Counter


def canonicalize_symbol(symbol: str) -> str:
    # Step 1: Parsing
    units = re.findall(r'([a-zA-Z]+)(?:\^(-?\d+))?', symbol)

    # Step 2: Sorting and Counting
    unit_counter = Counter()
    for unit, power in units:
        power = int(power) if power else 1
        unit_counter[unit] += power

    # Step 3: Formatting
    sorted_units = sorted(unit_counter.items())
    canonical_symbol = '*'.join(f"{unit}^{power}" if power != 1 else unit for unit, power in sorted_units)

    return canonical_symbol
