#!/usr/bin/env python3
""" A Union and Tuple function """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return Tuple of string and float """
    return (k, v**2)
