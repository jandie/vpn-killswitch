import killer

import psutil

import logger

import subprocess


class ProcessChecker():
    def __init__(self):
        pass

    def is_running(self, process_name):
        try:
            pids = psutil.pids()

            for pid in pids:
                if process_name == self.get_process_name(pid):
                    return True
        except Exception, e:
            print e.message

        return False

    def get_process_name(self, pid):
        p = psutil.Process(pid)
        return p.name()

    def check_p2p_processes(self):
        if not self.is_running('qbittorrent'):
            p = subprocess.Popen(['qbittorrent'], close_fds=True)

            logger.log('Started qBitTorrent')

        if not self.is_running('WebTorrent'):
            subprocess.Popen(['/opt/webtorrent-desktop/WebTorrent'], close_fds=True)

            logger.log('Started WebTorrent')
