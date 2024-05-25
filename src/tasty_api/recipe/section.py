from dataclasses import dataclass

from tasty_api.recipe import Component


@dataclass(frozen=True, slots=True)
class Section:
    """Represents a part of a recipe."""

    components: list[Component]
    name: str | None
    position: int
