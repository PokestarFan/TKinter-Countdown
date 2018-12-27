"""This module defines the errors in the Countdown module."""


class CountdownError(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class InvalidTimeError(CountdownError):
    def __init__(self, time: int, *args: object, **kwargs: object) -> None:
        super().__init__(*args, '\nInputted time: %d second(s)' % time, **kwargs)


class TooLittleTimeError(InvalidTimeError):
    def __init__(self, time: int, *args: object, **kwargs: object) -> None:
        super().__init__(time, 'The inputted time value is less than one second.', *args, **kwargs)


class TooMuchTimeError(InvalidTimeError):
    def __init__(self, time: int, *args: object, **kwargs: object) -> None:
        super().__init__(time, 'The inputted time value results in a date larger than December 31, 2099.',
                         *args, **kwargs)
