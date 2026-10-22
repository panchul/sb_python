'''
  % python ctx_mgr.py
  Opening resource
    calling yield, the resource is ready
  Using resource
  Using resource more
  Closing resource
'''

from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Opening resource")
    try:
        print("  calling yield, the resource is ready")
        yield
    finally:
        print("Closing resource")

with managed_resource():
    print("Using resource")
    print("Using resource more")

