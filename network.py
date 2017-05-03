import re

import duckduckgo

from killer import TimeOutKiller


class Network:
    def __init__(self, logger, killer, time_out):
        self.logger = logger
        self.killer = killer
        self.time_out = time_out

    def retrieve_ip_from_ddg(self):
        r = duckduckgo.query('my ip')
        return re.findall(r'[0-9]+(?:\.[0-9]+){3}', r.answer.text)[0]

    def get_my_ip(self):
        try:
            with TimeOutKiller(self.time_out, self.killer):
                return self.retrieve_ip_from_ddg()
        except Exception, e:
            self.logger.log(e)

            return '-1'
