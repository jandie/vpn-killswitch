import time
import config
from logger import Logger
from killer import Killer
from network import Network


my_config = config.load()
logger = Logger()
killer = Killer(logger)
network = Network(logger)
seconds_to_wait = 10

while True:

    ip = network.get_my_ip()

    logger.log(ip)

    if ip == '-1' or ip == '':
        killer.kill_processes(my_config.get_processes())

    if ip == my_config.get_wrong_ip():
        killer.kill_processes(my_config.get_processes())

    time.sleep(seconds_to_wait)
