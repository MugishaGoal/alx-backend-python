#!/usr/bin/env python3
"""The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator [float, None, None]:
    """Coroutine that yields random numbers asynchronously"""
    for _ in range(10):
        await async.sleep(1)
        yield random.random() * 10
