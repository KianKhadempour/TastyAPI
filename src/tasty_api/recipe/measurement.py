from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Unit:
    """Represents the unit of a `Measurement`."""

    abbreviation: str
    display_plural: str
    display_singular: str
    name: str
    system: str | None


@dataclass(frozen=True, slots=True)
class Measurement:
    """Represents the amount of a `Component`."""

    id: int
    quantity: float
    unit: Unit
