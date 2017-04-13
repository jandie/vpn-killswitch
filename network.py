import re

import duckduckgo


class Network:
    def __init__(self, logger):
        self.logger = logger

    def get_my_ip(self):
        try:
            r = duckduckgo.query('my ip')
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', r.answer.text)[0]
        except Exception, e:
            self.logger.log(e.message)
            ip = '-1'

        return ip