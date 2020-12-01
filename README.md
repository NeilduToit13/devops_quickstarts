# devops_quickstarts
Short scripts for getting started with devops tasks at AfricanLII

# Simple RPC server
The simple RPC server and client creates and RPC server using python's multiprocessing library.
This is, in my experience, a much quicker way to plumb between services in cases 
where the server is not expected to ever require third party integration.

The RPC server also performs well as a cache or task queue, without requiring third party services like celery, which adds a large devops overead. It essential allows you to share memory-state between requests in web context.

The functionality is not well documented, but it is powerful. For an overview of 
some of these functions of the multiprocessing library, see https://www.usenix.org/system/files/login/articles/login1210_beazley.pdf

runtime: python3.8
There are no external dependencies
