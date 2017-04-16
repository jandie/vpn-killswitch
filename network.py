import re
import signal
from contextlib import contextmanager

import duckduckgo


@contextmanager
def timeout(seconds):
    def timeout_handler(signum, frame):
        pass

    original_handler = signal.signal(signal.SIGALRM, timeout_handler)

    try:
        signal.alarm(seconds)
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, original_handler)


class Network:
    def __init__(self, logger):
        self.logger = logger

    def retrieve_ip_from_ddg(self):
        try:
            r = duckduckgo.query('my ip')
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', r.answer.text)[0]
        except Exception, e:
            self.logger.log(e.message)
            ip = '-1'

        return ip

    def get_my_ip(self):
        try:
            with timeout(2):
                return self.retrieve_ip_from_ddg()
        except Exception, e:
            self.logger.log(e)

            return '-1'
