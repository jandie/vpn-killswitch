import threading
import time

import psutil


class TimeOutKiller(threading.Thread):
    def __init__(self, timeout, killer):
        threading.Thread.__init__(self)
        self.timeout = timeout
        self.setDaemon(True)
        self.cancel = False
        self.killer = killer

    def run(self):
        counter = 0

        try:
            while self.cancel:
                time.sleep(1)
                counter += 1

                if self.cancel:
                    raise RuntimeError()

                if counter > self.timeout and not self.cancel:
                    self.killer.kill_processes()
        except RuntimeError:
            pass  # ignore

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cancel = False

class Killer:
    def __init__(self, logger, processes):
        self.logger = logger
        self.processes = processes

    def kill_process(self, name):

        try:
            for process in psutil.process_iter():
                if process.name() == name:
                    self.logger.log(
                        'Killing ' + name + ' process...')
                    process.kill()

        except Exception, e:
            print self.logger.log(e.message)

    def kill_processes(self):
        for process in self.processes:
            self.kill_process(process)
