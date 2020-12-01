from multiprocessing.managers import BaseManager
import logging 

# Create a logger
formatter = logging.Formatter(fmt='%(asctime)s-%(module)s-%(levelname)s ==> %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log = logging.getLogger('root')
log.setLevel("DEBUG")
log.addHandler(handler)

PORT = 8000

if __name__ == "__main__":
    manager = BaseManager(('127.0.0.1', PORT), b'password')
    manager.register('foo')
    manager.connect()

    log.info("Calling foo at the server")

    result = manager.foo(2,3)
    
    log.info(f"result: {result}")
