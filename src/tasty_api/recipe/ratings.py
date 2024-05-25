from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Ratings:
    count_negative: int
    count_positive: int
    score: int  # TODO: Check if it's a float
