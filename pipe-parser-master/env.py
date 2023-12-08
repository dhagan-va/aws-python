import os
import sys


def envdef(name, default):
    try:
        _ = os.environ[name]
    except:
        _ = default
    return _


def envreq(name):
    try:
        return os.environ[name]
    except:
        print(f"{name} is required")
        sys.exit(2)
