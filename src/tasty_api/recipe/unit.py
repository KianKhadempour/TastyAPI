from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Unit:
    abbreviation: str
    display_plural: str
    display_singular: str
    name: str
    system: str | None
