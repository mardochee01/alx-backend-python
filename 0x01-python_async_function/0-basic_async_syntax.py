#!/usr/bin/env python3
"""basic of async"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
