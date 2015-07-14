import sys

__author__ = 'Johan Vergeer'

'''A module for demonstrating exceptions'''

def convert(s):
    """Convert to an integer"""
    try:
        return int(s)
    except  (ValueError, TypeError) as e:
        print("Conversion error: {}"\
              .format(str(e)),
              file = sys.stderr)
    return
