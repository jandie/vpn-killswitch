import duckduckgo
import time
from logger import Logger
from killer import Killer


def load_wrong_answer():
    try:
        with open('wrong.txt', 'r') as the_file:
            return the_file.readline()
    except Exception, e:
        Logger().log(e.message)
        exit()

logger = Logger()
killer = Killer(logger)

wrong_answer = load_wrong_answer()
seconds_to_wait = 10

while True:

    try:
        r = duckduckgo.query('my ip')
    except Exception, e:
        logger.log(
            'Something went wrong while accessing DDG: ' +
            e.message)

        killer.kill_p2p_processes()

    logger.log(r.answer.text)

    if r.answer.text == wrong_answer:
        killer.kill_p2p_processes()

    time.sleep(seconds_to_wait)
