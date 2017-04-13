import psutil


class Killer():
    def __init__(self, logger):
        self.logger = logger

    def kill_process(self, name):

        try:
            for proc in psutil.process_iter():
                if proc.name() == name:
                    self.logger.log(
                        'Killing ' + name + ' process...')
                    proc.kill()

        except Exception, e:
            print e.message

    def kill_processes(self, processes):
        for proces in processes:
            self.kill_process(proces)
