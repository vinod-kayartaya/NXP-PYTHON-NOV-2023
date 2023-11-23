"""
Some useful utility functions for future use.
"""


def dir2(obj) -> list:
    return [at for at in dir(obj) if not at.startswith('_')]

# dir2 = lambda obj: [at for at in dir(obj) if not at.startswith('_')]
# In Java:
# dir2 = obj -> return_value
# In Java:
# dir2 = obj => return_value
