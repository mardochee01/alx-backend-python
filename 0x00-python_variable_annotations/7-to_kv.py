#!/usr/bin/env python3
"""to_kv module"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to kv ubion"""
    return (k, v**2)
