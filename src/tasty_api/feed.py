from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from tasty_api.recipe import Recipe


@dataclass(frozen=True, slots=True)
class FeedItem:
    type: str
    recipe: Recipe

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> FeedItem:
        return FeedItem(type=data["type"], recipe=Recipe.from_dict(data["recipe"]))
