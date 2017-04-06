import duckduckgo
import os
from logger import Logger

FILE_NAME = 'wrong.txt'

try:
    r = duckduckgo.query('my ip')
except Exception, e:
    Logger().log(e)

wrong_answer = r.answer.text

if os.path.isfile(FILE_NAME):
    os.remove(FILE_NAME)

with open(FILE_NAME, 'a') as the_file:
    the_file.write(wrong_answer)
