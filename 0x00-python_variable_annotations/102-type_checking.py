#!/usr/bin/env python3
"""Zoom in on the elements of the input list by repeating each element"""


from typing import Tuple, List, Iterable


def zoom_array(lst: Iterable, factor: int = 2) -> List:
    "Zoom in on the elements of the input list by repeating each element"
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
