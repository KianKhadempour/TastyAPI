from dataclasses import dataclass

from tasty_api.recipe import (
    Instruction,
    Nutrition,
    Price,
    Ratings,
    RecipeMetadata,
    Section,
    Topic,
)
from tasty_api.tag import Tag  # Doesn't exist yet but it will


@dataclass(frozen=True, slots=True)
class Recipe:
    """Represents a recipe."""

    metadata: RecipeMetadata
    cook_time_minutes: int | None
    description: str
    instructions: list[Instruction]
    name: str
    num_servings: int
    nutrition: Nutrition
    prep_time_minutes: int | None
    price: Price
    sections: list[Section]
    tags: list[Tag]
    topics: list[Topic]
    total_time_minutes: int | None
    user_ratings: Ratings
    yields: str
