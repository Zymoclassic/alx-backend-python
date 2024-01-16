#!/usr/bin/env python3
"""
the basics of async
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    returns a random number after random seconds
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
