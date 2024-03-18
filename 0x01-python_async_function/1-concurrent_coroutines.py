#!/usr/bin/env python3
"""An async routine called wait_n that takes in 2 int arguments"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
