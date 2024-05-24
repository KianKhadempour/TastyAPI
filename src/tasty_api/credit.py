from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Credit:
    name: str | None
    type: str
