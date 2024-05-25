from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Nutrition:
    """Represents the nutrition facts of a recipe. All values are in grams."""

    calories: int
    carbohydrates: int
    fat: int
    fiber: int
    protein: int
    sugar: int
    updated_at: datetime
