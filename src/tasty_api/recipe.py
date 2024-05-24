from dataclasses import dataclass

import pycountry
import pycountry.db

from tasty_api import Credit

pycountry.countries


@dataclass(frozen=True, slots=True)
class Recipe:
    approved_at: int
    aspect_ratio: str
    beauty_url: str | None
    brand: str | None
    brand_id: int | None
    buzz_id: int | None
    canonical_id: str
    compilations: list[SOMETHING]
    cook_time_minutes: int | None
    country: pycountry.db.Country
    created_at: int
    credits: list[Credit]
    description: str
    draft_status: str
    facebook_posts: list[SOMETHING]
    id: int
    inspired_by_url: str
    instructions: list[Instruction]
