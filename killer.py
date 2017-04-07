import commands


class Killer():
    def __init__(self, logger):
        self.logger = logger
        pass

    def kill_process(self, name):
        try:
            commands.getoutput('pkill -f ' + name)
            self.logger.log('Killed ' + name + ' process')
        except Exception, e:
            print e.message

    def kill_processes(self, processes):
        for proces in processes:
            self.kill_process(proces)
