#!/usr/bin/env python3
"""Return the first element of a sequence safely"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    "Returns The first element of the sequence if it exists, else None"
    if lst:
        return lst[0]
    else:
        return None
