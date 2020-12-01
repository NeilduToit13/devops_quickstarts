"""Simple starter script for creating an RPC server with multiprocessing
"""
from multiprocessing.managers import BaseManager 


PORT = 8000


def foo(num1: int, num2: int):
    return num1 + num2


if __name__ == "__main__":
    manager = BaseManager(('', PORT), b'password')
    manager.register('foo', foo)
    server = manager.get_server()
    print(f"server will now server on port {PORT}")
    server.serve_forever()
