import re

import duckduckgo

from killer import TimeOutKiller


class Network:
    def __init__(self, logger, killer):
        self.logger = logger
        self.killer = killer

    def retrieve_ip_from_ddg(self):
        r = duckduckgo.query('my ip')
        return re.findall(r'[0-9]+(?:\.[0-9]+){3}', r.answer.text)[0]

    def get_my_ip(self):
        try:
            with TimeOutKiller(10, self.killer):
                return self.retrieve_ip_from_ddg()
        except Exception, e:
            self.logger.log(e)

            return '-1'
