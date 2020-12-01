# devops_quickstarts
Short scripts for getting started with devops tasks at AfricanLII

# Python Tests Git Hook
git hooks can be any executable code. Python scripts can therefore be used, provided Python3 is available in /usr/bin/env This allows hooks to be used as an effective CI without the need for external tools like travis/jenkins
In this example, the hook, along with a short script and testing code are included. The hook will run the tests, and abort the commit if they fail. This hook has also been copied into the git hooks directory for THIS repository, so that they will be run when committing to this repository, as a POC.




# Simple RPC server
The simple RPC server and client creates and RPC server using python's multiprocessing library.
This is, in my experience, a much quicker way to plumb between services in cases 
where the server is not expected to ever require third party integration.

The RPC server also performs well as a cache or task queue, without requiring third party services like celery, which adds a large devops overead. It essential allows you to share memory-state between requests in web context.

The functionality is not well documented, but it is powerful. For an overview of 
some of these functions of the multiprocessing library, seehttps:
- https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager
- https://www.usenix.org/system/files/login/articles/login1210_beazley.pdf
Note that no locks are used in this example but may be necessary when the function holds a resource:
- https://pymotw.com/2/multiprocessing/communication.html

runtime: python3.8
There are no external dependencies
