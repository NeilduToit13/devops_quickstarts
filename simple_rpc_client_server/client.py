"""Multiprocessing RPC server client quickstart
"""

from multiprocessing.managers import BaseManager


PORT = 8000

if __name__ == "__main__":
    manager = BaseManager(('127.0.0.1', PORT), b'password')
    manager.register('foo')
    manager.connect()

    print("Calling foo at the server")
    result = manager.foo(2,3)
    print(f"result: {result}")
