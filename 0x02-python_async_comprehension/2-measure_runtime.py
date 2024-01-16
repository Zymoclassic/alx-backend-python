#!/usr/bin/env python3
"""
measure runtime
"""
import asyncio
import time
from importlib import import_module as theModule

async_comprehension = theModule('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes the function four times
    """
    startTime = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.time() - startTime
