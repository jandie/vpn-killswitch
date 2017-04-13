import psutil


class Killer:
    def __init__(self, logger):
        self.logger = logger

    def kill_process(self, name):

        try:
            for process in psutil.process_iter():
                if process.name() == name:
                    self.logger.log(
                        'Killing ' + name + ' process...')
                    process.kill()

        except Exception, e:
            print self.logger.log(e.message)

    def kill_processes(self, processes):
        for process in processes:
            self.kill_process(process)
