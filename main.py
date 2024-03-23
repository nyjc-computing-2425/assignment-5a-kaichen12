
def to_hms(seconds: int) -> list:
    """
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated

    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
    """
    # Type your code below
    if type(seconds) != int or seconds < 0:
        print('Unsupported input type.')
    else:
        hours, remain_sec = divmod(seconds,3600)
        mins, secs = divmod(remain_sec,60)
        return [hours, mins, secs]
