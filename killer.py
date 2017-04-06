import commands
from logger import Logger


class Killer():
    def __init__(self, logger):
        self.logger = logger
        pass

    def kill_p2p_processes(self):
        try:
            commands.getoutput('pkill -f webtorrent')
            self.logger.log('Killed WebTorrent process')

            commands.getoutput('pkill -f qbittorrent')
            self.logger.log('Killed qBitTorrent process')
        except Exception, e:
            print e.message
