from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from dataclass_wizard import JSONWizard

from tasty_api.recipe import Completion, Recipe


@dataclass
class CompletionData(JSONWizard):
    """JSONWizard to destructure auto complete requests."""

    class _(JSONWizard.Meta):
        debug_enabled = True
        key_transform_with_dump = "SNAKE"

    results: list[Completion]


@dataclass(frozen=True, slots=True)
class RecipeListData:
    """Custom class to destructure recipe/list requests."""

    count: int
    results: list[Recipe]

    # TODO (maybe): Replace the Any with the full type of the dictionary. Big maybe.
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RecipeListData:
        return RecipeListData(
            data["count"], [Recipe.from_dict(result) for result in data["results"]]
        )
