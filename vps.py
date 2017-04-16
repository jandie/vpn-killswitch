import time

import config
from killer import Killer
from logger import Logger
from network import Network

my_config = config.load()
logger = Logger()
killer = Killer(logger, my_config.get_processes())
network = Network(logger, killer)

while True:

    ip = network.get_my_ip()

    logger.log(ip)

    if ip == '-1' or ip == '':
        killer.kill_processes()

    if ip == my_config.get_wrong_ip():
        killer.kill_processes()

    time.sleep(float(my_config.get_frequency()))
