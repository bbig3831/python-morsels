from collections import deque


def tail(seq, n):
    """Return the last n items of a given iterable"""
    if n<= 0:
        return []
    return list(deque(seq, maxlen=n))