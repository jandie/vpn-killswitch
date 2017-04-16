import re
import threading
import time

import duckduckgo


class TimeOut(threading.Thread):
    def __init__(self, timeout, killer):
        threading.Thread.__init__(self)
        self.timeout = timeout
        self.setDaemon(True)
        self.raise_error = True
        self.killer = killer

    def run(self):
        time.sleep(self.timeout)

        if self.raise_error:
            self.killer.kill_processes()
            raise RuntimeError("Timeout!")

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.raise_error = False


class Network:
    def __init__(self, logger, killer):
        self.logger = logger
        self.killer = killer

    def retrieve_ip_from_ddg(self):
        r = duckduckgo.query('my ip')
        return re.findall(r'[0-9]+(?:\.[0-9]+){3}', r.answer.text)[0]

    def get_my_ip(self):
        try:
            with TimeOut(1, self.killer):
                return self.retrieve_ip_from_ddg()
        except Exception, e:
            self.logger.log(e)

            return '-1'
