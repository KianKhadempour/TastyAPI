from dataclasses import dataclass
from datetime import datetime

import iso639
import pycountry.db

from tasty_api.recipe import Credit


@dataclass(frozen=True, slots=True)
class RecipeMetadata:
    approved_at: datetime
    aspect_ratio: str
    beauty_url: str | None
    brand: str | None
    brand_id: int | None
    buzz_id: int | None
    canonical_id: str
    # TODO (when I find an example): compilations: list[SOMETHING]
    country: pycountry.db.Country
    created_at: datetime
    credits: list[Credit]
    draft_status: str
    # TODO (when I find an example): facebook_posts: list[SOMETHING]
    id: int
    inspired_by_url: str | None
    is_app_only: bool
    is_one_top: bool
    is_shoppable: bool
    is_subscriber_content: bool
    keywords: str
    language: iso639.Language
    nutrition_visibility: str
    original_video_url: str | None
    promotion: str
    # TODO (when I find an example):renditions: list[SOMETHING]
    seo_path: str
    seo_title: str
    servings_noun_plural: str
    servings_noun_singular: str
    show_name: str
    show_id: int
    slug: str
    thumbnail_alt_text: str
    thumbnail_url: str
    tips_and_ratings_enabled: bool
    # TODO (when I find an example):total_time_tier: SOMETHING | None
    updated_at: datetime
    # TODO (when I find an example):video_ad_content: SOMETHING | None
    video_id: int | None
    video_url: str | None
