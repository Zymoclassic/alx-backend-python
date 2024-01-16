#!/usr/bin/env python3
"""
async comprehension
"""
import asyncio
import random
from typing import Generator
from typing import List
from importlib import import_module as theModule

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    create random list of 10 numbers
    """
    return [x async for x in async_generator()]
