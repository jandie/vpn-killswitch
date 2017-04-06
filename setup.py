import os
from logger import Logger
from network import Network

FILE_NAME = 'wrong.txt'

wrong_ip = Network().get_my_ip(Logger())

if os.path.isfile(FILE_NAME):
    os.remove(FILE_NAME)

with open(FILE_NAME, 'a') as the_file:
    the_file.write(wrong_ip)
