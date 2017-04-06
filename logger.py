import datetime


class Logger():
    def __init__(self):
        pass

    def log(self, message):
        output = str(datetime.datetime.now()) + ' ' + message

        with open('log.txt', 'a') as the_file:
            the_file.write(output + '\n')

        print output
