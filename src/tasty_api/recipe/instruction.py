from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Instruction:
    """Represents a single step in the recipe's instructions."""

    appliance: str | None
    display_text: str
    end_time: int
    id: int
    position: int
    start_time: int
    # TODO (when I find an example): temperature: SOMETHING | None
