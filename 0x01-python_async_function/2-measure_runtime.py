#!/usr/bin/env python3
"""A a measure_time function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and returns
total_time / n"""


import time
from typing import List
from asyncio import run
from functools import wraps


wait_n = __import__('1-concurrent_coroutines').waitmon

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay), and return total_time / n.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        float: The average execution time per call.
    """
    @wraps(wait_n)
    async def wrapped_wait_n(n: int, max_delay: int) -> List[float]:
        start_time = time.time()
        await wait_n(n, max_delay)
        end_time = time.time()
        return end_time - start_time

    total_time = run(wrapped_wait_n(n, max_delay))
    return total_time / n
