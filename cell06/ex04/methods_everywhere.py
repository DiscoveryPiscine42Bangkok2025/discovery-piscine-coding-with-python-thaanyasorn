#!/usr/bin/env python3
import sys

def shrink(text):
    return text[:8]

def enlarge(text):
    return text + "Z" * (8 - len(text))

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            print(shrink(arg))
        elif len(arg) < 8:
            print(enlarge(arg))
        else:
            print(arg)
