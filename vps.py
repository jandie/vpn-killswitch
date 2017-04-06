import time
from logger import Logger
from killer import Killer
from network import Network


def load_wrong_ip():
    try:
        with open('wrong.txt', 'r') as the_file:
            return the_file.readline()
    except Exception, e:
        Logger().log(e.message)
        exit()

logger = Logger()
killer = Killer(logger)
network = Network(logger)

wrong_ip = load_wrong_ip()
seconds_to_wait = 10

while True:

    ip = network.get_my_ip()

    logger.log(ip)

    if ip == '':
        killer.kill_p2p_processes()

    if ip == wrong_ip:
        killer.kill_p2p_processes()

    time.sleep(seconds_to_wait)
