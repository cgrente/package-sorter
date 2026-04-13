"""Package dispatch logic for Smarter Technology's robotic sorting arm."""

# Thresholds from the specification
BULKY_VOLUME_CM3 = 1_000_000
BULKY_DIMENSION_CM = 150
HEAVY_MASS_KG = 20

def sort(width: float, height: float, length: float, mass: float) -> str:
    """Dispatch a package to the correct stack based on its dimensions and mass.

    A package is bulky if its volume is >= 1,000,000 cm³ or any single
    dimension is >= 150 cm. A package is heavy if its mass is >= 20 kg.

    Returns:
        "REJECTED" if both heavy and bulky,
        "SPECIAL"  if either heavy or bulky,
        "STANDARD" otherwise.
    """
    if min(width, height, length) <= 0:
        raise ValueError(f"Dimension must be positive, got width={width}, height={height}, length={length}")
    if mass < 0:
        raise ValueError(f"Mass cannot be negative, got {mass}")

    package_volume = width * height * length
    is_bulky = (
            package_volume >= BULKY_VOLUME_CM3 or
            max(width, height, length) >= BULKY_DIMENSION_CM
    )
    is_heavy = mass >= HEAVY_MASS_KG

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"

    return "STANDARD"