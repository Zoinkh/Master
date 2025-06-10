import os
import sys
import time
import signal

def daemonize(pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    """
    Daemonize the current process.
    """

    # First fork (detaches from parent)
    try:
        pid = os.fork()
        if pid > 0:
            # Exit first parent
            sys.exit(0)
    except OSError as err:
        sys.stderr.write(f'fork #1 failed: {err}\n')
        sys.exit(1)

    # Decouple from parent environment
    os.chdir('/')
    os.setsid()
    os.umask(0)

    # Second fork (relinquish session leadership)
    try:
        pid = os.fork()
        if pid > 0:
            # Exit second parent
            sys.exit(0)
    except OSError as err:
        sys.stderr.write(f'fork #2 failed: {err}\n')
        sys.exit(1)

    # Redirect standard file descriptors
    sys.stdout.flush()
    sys.stderr.flush()
    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'a+')

    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

    # Write pidfile
    with open(pidfile, 'w+') as f:
        print(os.getpid(), file=f)

    # Register signal handlers
    def sigterm_handler(signum, frame):
        sys.exit(0)

    signal.signal(signal.SIGTERM, sigterm_handler)

def main():
    """
    Daemon main loop.
    """
    while True:
        # Your daemon's core logic goes here
        print(f"Daemon running at {time.ctime()}")
        time.sleep(5)

if __name__ == '__main__':
    pidfile = '/tmp/mydaemon.pid'  # Change to your desired pidfile location
    daemonize(pidfile)
    main()