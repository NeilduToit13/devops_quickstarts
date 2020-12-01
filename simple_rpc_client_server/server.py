"""Simple starter script for creating an RPC server with multiprocessing
"""

from multiprocessing.managers import BaseManager 
from multiprocessing import Lock

import logging 

# Create a logger
formatter = logging.Formatter(fmt='%(asctime)s-%(module)s-%(levelname)s ==> %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log = logging.getLogger('root')
log.setLevel("DEBUG")
log.addHandler(handler)

connections = {}
lock = Lock()

PORT = 8000


def foo(num1: int, num2: int):
    return num1 + num2



if __name__ == "__main__":
    manager = BaseManager(('', PORT), b'password')
    manager.register('foo', foo)
    server = manager.get_server()
    log.info(f"server will now server on port {PORT}")
    server.serve_forever()
