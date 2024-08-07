#!/usr/bin/env python3
""" asyncio Task """
from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> Task:
    """ RETURNS A TASK """
    task = create_task(wait_random(max_delay))
    return task
