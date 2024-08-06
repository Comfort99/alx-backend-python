#!/usr/bin/env python3
""" asynchronous coroutine """
import asyncio
import random


async def wait_random(mex_delay: int = 10) -> float:
    """ coroutine that takes in an integer argument
      Waits for a random delay between 0 and max_delay
      seconds and eventually returns it
      """
    delay = random.uniform(0, mex_delay)
    await asyncio.sleep(delay)
    return delay
