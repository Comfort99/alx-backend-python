#!/usr/bin/env python3
"""  elapsed time """
import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time for wait_n
    returns total_time / n """
    s = time()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time() - s
    total_time = elapsed / n
    return total_time
