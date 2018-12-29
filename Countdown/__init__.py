"""Countdown is a module with a easy countdown timer with two methods of input. """

import logging
from atexit import register
from datetime import datetime
from os import chdir, getcwd, mkdir
from os.path import isdir

DEBUG = True


def create_logger(name='Countdown'):
    logger = logging.getLogger(name)
    if DEBUG:
        if getcwd().split('\\')[-1] == 'Countdown':
            chdir('..')
            if not isdir('logs'):
                mkdir('logs')
            chdir('logs')
        with open('created.txt', 'a+') as file:
            if len(file.read()) > 0:
                dt = file.read()

                @register
                def wipe_file():
                    open('created.txt', 'w').close()
            else:
                dt = datetime.now().strftime('%D %T').replace('/', '-').replace(':', '-')
                file.write(dt)

        h, f = logging.StreamHandler(), logging.Formatter('%(asctime)s - %(pathname)s - %(levelname)s - %(message)s')
        h.setFormatter(f)
        h2 = logging.FileHandler('Countdown %s.log' % dt)
        h2.setFormatter(f)
        logger.addHandler(h)
        logger.addHandler(h2)
        logger.setLevel(logging.DEBUG)
    else:
        logger.addHandler(logging.NullHandler())
        logger.setLevel(logging.CRITICAL)
    return logger
