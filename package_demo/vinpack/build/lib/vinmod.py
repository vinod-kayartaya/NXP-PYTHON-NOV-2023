"""
Some useful utility functions for future use.
"""


def dir2(obj) -> list:
    """
    same as dir() method with out dunder attributes
    """
    return [at for at in dir(obj) if not at.startswith('_')]