#!/usr/bin/env python3
"""Safely get a value from a dictionary"""


from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: T = None
) -> Union[Any, T]:
    "Safely get a value from a dictionary"
    if key in dct:
        return dct[key]
    else:
        return default
