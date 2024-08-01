#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes a float multiplier as argument,
        Returns a function that multiplies a float by multiplier.
    """
    def f(n: float) -> float:
        """ Multiplies a float by multiplier """
        return float(n * multiplier)

    return f
