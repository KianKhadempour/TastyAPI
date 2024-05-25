from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Ingredient:
    """Represents an ingredient."""

    created_at: datetime
    display_plural: str
    display_singular: str
    id: int
    name: str
    updated_at: datetime
