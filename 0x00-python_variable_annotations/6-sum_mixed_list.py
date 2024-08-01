#!/usr/bin/env python3
""" A function that return a float """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sum of union types """
    
    return float(sum(mxd_lst))
