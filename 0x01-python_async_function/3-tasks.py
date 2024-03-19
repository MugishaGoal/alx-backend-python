#!/usr/bin/env python3
"""A function that takes an integer max_delay and returns a asyncio.Task"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> asyncio.Task[None]:
    """
    Create an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        Task[None]: An asyncio.Task for wait_random(max_delay).
    """
    async def wrapped_wait_random(max_delay: int) -> None:
        await wait_random(max_delay)

    return asyncio.create_task(wrapped_wait_random(max_delay))
