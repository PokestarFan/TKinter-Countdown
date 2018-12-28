from datetime import datetime

from Countdown import create_logger
from .consts import second, minute, hour, day, week, month, year
from .error import TooLittleTimeError, TooMuchTimeError

logger = create_logger('TC')


class TimeCalculator(object):
    """A class to retrieve the differences based on the amount of seconds in it."""

    def __init__(self, seconds: int):
        """Initializes the class

        :param seconds: The amount of seconds to process
        :type seconds: int
        """
        self.wordstr = ''
        self.run_main(seconds)

    def run_main(self, seconds: int):
        """The same thing as init, code from init to here in order to allow class inheritance."""
        self.timedict = {'sec': seconds}
        self.seconds = seconds
        if seconds < second:
            raise TooLittleTimeError(seconds)
        elif not isinstance(seconds, int):
            raise ValueError('Seconds needs to be int, not %s' % seconds.__class__.__name__)
        elif minute < seconds < hour:
            self.min_sec()
        elif hour < seconds < day:
            self.hr_min_sec()
        elif day < seconds < week:
            self.dy_hr_min_sec()
        elif week < seconds < month:
            self.wk_dy_hr_min_sec()
        elif month < seconds < year:
            self.mn_wk_dy_hr_min_sec()
        elif year < seconds < year * (2100 - datetime.now().year):
            self.yr_mn_wk_dy_hr_min_sec()
        elif seconds > year * (2100 - datetime.now().year):
            raise TooMuchTimeError(seconds)
        else:
            raise ValueError(
                'Seconds is not a normal integer, is %s with value %s' % (seconds.__class__.__name__, seconds))
        self.clean_dict()
        self.dict_to_word()

    def min_sec(self):
        self.timedict['min'], self.timedict['sec'] = divmod(self.seconds, minute)

    def hr_min_sec(self):
        self.min_sec()
        self.timedict['hr'], self.timedict['min'] = divmod(self.timedict['min'], hour)

    def dy_hr_min_sec(self):
        self.hr_min_sec()
        self.timedict['dy'], self.timedict['hr'] = divmod(self.timedict['hr'], day)

    def wk_dy_hr_min_sec(self):
        self.dy_hr_min_sec()
        self.timedict['wk'], self.timedict['dy'] = divmod(self.timedict['dy'], week)

    def mn_wk_dy_hr_min_sec(self):
        self.wk_dy_hr_min_sec()
        self.timedict['mn'], self.timedict['wk'] = divmod(self.timedict['wk'], month)

    def yr_mn_wk_dy_hr_min_sec(self):
        self.mn_wk_dy_hr_min_sec()
        self.timedict['yr'], self.timedict['mn'] = divmod(self.timedict['mn'], year)

    def clean_dict(self):
        kvpairs = [(key, item) for key, item in self.timedict.items()]
        for k, i in kvpairs:
            if i == 0:
                del self.timedict[k]
        logger.debug(self.timedict)

    def dict_to_word(self):
        for a, b in self.timedict.items():
            self.wordstr += '%d %s' % (b, a)
        logger.debug('Word string is %s', self.wordstr)
