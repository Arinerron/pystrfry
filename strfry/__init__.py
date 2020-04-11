#!/usr/bin/env python3

from ctypes import *
import time


cdll.LoadLibrary('libc.so.6')
libc = CDLL('libc.so.6')


# setup the types / structs


'''
struct random_data
  {
    int32_t *fptr;                /* Front pointer.  */
    int32_t *rptr;                /* Rear pointer.  */
    int32_t *state;                /* Array of state values.  */
    int rand_type;                /* Type of random number generator.  */
    int rand_deg;                /* Degree of random number generator.  */
    int rand_sep;                /* Distance between front and rear.  */
    int32_t *end_ptr;                /* Pointer behind state table.  */
  };
'''
class random_data(Structure):
    _fields_ = [
        ('fptr', POINTER(c_int)),
        ('rptr', POINTER(c_int)),
        ('state', POINTER(c_int)),
        ('rand_type', c_int),
        ('rand_deg', c_int),
        ('rand_sep', c_int),
        ('end_ptr', c_int)
    ]

rdata_type = c_char_p * 4
libc.initstate_r.argtypes = [c_int, rdata_type, c_int, POINTER(random_data)]
libc.random_r.argtypes = [POINTER(random_data), POINTER(c_int)]


# stdlib state


init = False
rdata = random_data()
state = None

def _reset_strfry():
    init = False
    rdata = random_data()
    state = None


def _init_random_state(ts = None, pid = None):
    global init, rdata, state

    _reset_strfry()

    ts = ts or int(time.time())
    pid = pid or libc.getpid()

    # init state
    state = rdata_type()
    rdata.state = None
    libc.initstate_r(c_int(ts ^ pid), state, sizeof(state), byref(rdata))
    init = True

    return rdata


# useful functions


'''
strfry - randomize a string
arg string: the str to create the anagram from
arg ts: an int representing the timestamp to use for randomness, if known
arg pid: an int representing the pid of the process which called strfry, if known
arg reset: whether or not to forcefully reset the random state
'''
def strfry(string, ts = None, pid = None, reset = True):
    global init, rdata, state

    _initial_type_is_str = isinstance(string, str)
    string = list(string)

    if (not init) or reset:
        _init_random_state(ts = ts, pid = pid)

    # actual strfry mess :(((
    for i in range(len(string)):
        j = c_int()
        libc.random_r(byref(rdata), byref(j))
        j = j.value % (len(string) - i) + i

        c = string[i]
        string[i] = string[j]
        string[j] = c

    # allow us to strfry symbols
    if _initial_type_is_str:
        return ''.join(string)
    else:
        return string

'''
strfry - unrandomize a string :sunglasses:
arg string: the str anagram to decode
arg ts: an int representing the timestamp to use for randomness, if known
arg pid: an int representing the pid of the process which called strfry, if known
arg reset: whether or not to forcefully reset the random state
'''
def unstrfry(string, ts = None, pid = None, reset = True):
    global init, rdata, state

    string = list(string)

    # use symbols to map strfry
    seq = list(range(len(string)))
    seq = strfry(seq, ts = ts, pid = pid, reset = reset)
    seq_out = [''] * len(seq)

    for symbol, i in zip(seq, range(len(seq))):
        seq_out[symbol] = string[i]

    return ''.join(seq_out)


# i use arch btw

