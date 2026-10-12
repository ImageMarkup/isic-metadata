from __future__ import annotations

import difflib
from functools import cache
from typing import TYPE_CHECKING

from pydantic_core import PydanticCustomError

if TYPE_CHECKING:
    from enum import StrEnum


@cache
def _suggestions(hierarchy: type[StrEnum], value: str) -> list[str]:
    # a value with a colon is an attempt at a full path, so suggest full paths. otherwise suggest
    # terminal values, which is what accept_terminal_values resolves.
    candidates: dict[str, str] = {}
    for member in hierarchy:
        candidate = str(member) if ":" in value else member.split(":")[-1]
        candidates[candidate.lower()] = candidate
    return [candidates[match] for match in difflib.get_close_matches(value.lower(), candidates)]


def suggestion_error(kind: str, hierarchy: type[StrEnum], value: str) -> PydanticCustomError:
    """
    Build the error for a value that isn't in a hierarchy, suggesting close matches.

    pydantic's own enum error lists every member, which for a hierarchy of hundreds of values
    isn't a helpful message.
    """
    suggestions = [f"'{suggestion}'" for suggestion in _suggestions(hierarchy, value)]
    if not suggestions:
        return PydanticCustomError(
            "unknown_hierarchical_value",
            "Unknown {kind} '{value}'.",
            {"kind": kind, "value": value},
        )

    *head, last = suggestions
    return PydanticCustomError(
        "unknown_hierarchical_value",
        "Unknown {kind} '{value}'. Did you mean {suggestions}?",
        {
            "kind": kind,
            "value": value,
            "suggestions": f"{', '.join(head)} or {last}" if head else last,
        },
    )
