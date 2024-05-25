from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Credit:
    """Represents a credit (eg. author) of the recipe."""

    name: str | None
    type: str
