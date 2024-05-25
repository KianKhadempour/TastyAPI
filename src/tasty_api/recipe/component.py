from dataclasses import dataclass

from tasty_api.recipe import Ingredient, Measurement


@dataclass(frozen=True, slots=True)
class Component:
    """
    Collection of details surrounding an ingredient.
    Ex: 10 cloves peeled garlic
    """

    extra_comment: str
    id: int
    ingredient: Ingredient
    measurements: list[Measurement]
    position: int
    raw_text: str
