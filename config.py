import json
import os

import logger


class Config:
    def __init__(self, wrong_ip, frequency, processes):
        self.wrong_ip = wrong_ip
        self.frequency = frequency
        self.processes = processes

    def get_wrong_ip(self):
        return self.wrong_ip

    def get_frequency(self):
        return self.frequency

    def get_processes(self):
        return self.processes

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def as_config(dct):
    return Config(dct['wrong_ip'], dct['frequency'], dct['processes'])


def save(config_value):
    if os.path.isfile('config.txt'):
        os.remove('config.txt')

    j_string = config_value.to_json()

    with open("config.txt", "w") as the_file:
        the_file.write(j_string)


def load():
    try:
        with open("config.txt", "r") as the_file:
            cf = json.loads(the_file.read(), object_hook=as_config)

            print "Wrong_ip: " + cf.get_wrong_ip()
            print "Check frequency: " + cf.get_frequency()
            print "Processes to kill:"

            for name in cf.get_processes():
                print name

            return cf

    except Exception, e:
        logger.Logger().log("Error while loading config")
        logger.Logger().log(e.message)
        exit()
