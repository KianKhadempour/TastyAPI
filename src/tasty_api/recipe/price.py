from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Price:
    """Represents the price of a recipe in cents (probably USD)."""

    consumption_portion: int
    consumption_total: int
    portion: int
    total: int
    updated_at: datetime
