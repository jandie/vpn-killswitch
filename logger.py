import datetime


class Logger():
    def __init__(self):
        pass

    def log(self, message):
        try:
            output = str(datetime.datetime.now()) + ' ' + str(message)

            with open('log.txt', 'a') as the_file:
                the_file.write(output + '\n')

            print output
        except Exception, e:
            print e.message
