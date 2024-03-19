#!/usr/bin/env python3
"""An  an asyncio.Task for wait_random(max_delay)"""

import asyncio
from typing import Task
from asyncio import Task as asyncio_Task

wait_random = __import__('0-basic_async_syntax').wait_random  # Importing wait_random from the previous file

def task_wait_random(max_delay: int) -> Task[None]:
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