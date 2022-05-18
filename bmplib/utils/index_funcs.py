# list of useful functions for analysis

from numpy import where, abs, min


def tindex(time_arr, time_value, delta=2e-2):
    """ Outputs the index of given timevalue
    Inputs: timearr, timevalue, delta
        timearr: numpy array of time values
        timevalue: time value of interest
        delta: residual error for time value
    Outputs: tind
        tind: the index of corresponding to timevalue
    """
    tind = where(abs((time_arr)-(time_value)) < delta)
    tind = tind[0][0]
    return tind


def tindex_min(time_arr, time_value):
    min_val = min(abs((time_arr)-time_value))
    tind = where(abs((time_arr)-(time_value)) == min_val)
    tind = tind[0][0]
    return tind


def tindex_near(time_arr, time_value, threshold):
    tinds = where(abs(time_arr-time_value) < threshold)
    return tinds


def first_zero(time_arr):
    """ The first zero
    Inputs: timearr
        timearr: numpy array
    Outputs: tind
        zind: index of the first zero in timearr
    """
    for n in range(len(time_arr)):
        zind = n
        if time_arr[n] < 0:
            break
    return zind
