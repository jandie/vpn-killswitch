import json
import os
import logger


class Config(object):
    def __init__(self, wrong_ip, processes):
        self.wrong_ip = wrong_ip
        self.processes = processes

    def get_wrong_ip(self):
        return self.wrong_ip

    def get_processes(self):
        return self.processes

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def as_config(dct):
    return Config(dct['wrong_ip'], dct['processes'])


def save(config_value):
    if os.path.isfile('config.txt'):
        os.remove('config.txt')

    j_string = config_value.toJSON()

    with open("config.txt", "w") as the_file:
        the_file.write(j_string)


def load():
    try:
        with open("config.txt", "r") as the_file:
            cf = json.loads(the_file.read(), object_hook = as_config)

            print cf.get_wrong_ip()

            for name in cf.get_processes():
                print name

            return cf

    except Exception, e:
        logger.Logger().log(e.message)
        exit()
