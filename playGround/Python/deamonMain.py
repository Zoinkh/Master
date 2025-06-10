import daemon
import time
import sys
import os

def main():
    while True:
        print(f"Daemon running at {time.ctime()}")
        time.sleep(5)

if __name__ == '__main__':
    pidfile = '/tmp/mydaemon.pid'
    logfile = '/tmp/mydaemon.log'

    context = daemon.DaemonContext(
        working_directory=os.getcwd(),
        pidfile=daemon.pidfile.PidFile(pidfile),
        stdout=open(logfile, 'a+'),
        stderr=open(logfile, 'a+'),
    )

    with context:
        main()