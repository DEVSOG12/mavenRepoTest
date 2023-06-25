# Copyright (c) 2008 - 2022, Ilan Schnell; All Rights Reserved
"""
This package defines an object type which can efficiently represent
a bitarray.  Bitarrays are sequence types and behave very much like lists.

Please find a description of this package at:

    https://github.com/ilanschnell/bitarray

Author: Ilan Schnell
"""
from __future__ import absolute_import

from bitarray._bitarray import (bitarray, decodetree, _sysinfo,
                                get_default_endian, _set_default_endian,
                                __version__)


__all__ = ['bitarray', 'frozenbitarray', 'decodetree', '__version__']


class frozenbitarray(bitarray):
    """frozenbitarray(initializer=0, /, endian='big', buffer=None) -> \
frozenbitarray

Return a frozenbitarray object, which is initialized the same way a bitarray
object is initialized.  A frozenbitarray is immutable and hashable.
Its contents cannot be altered after it is created; however, it can be used
as a dictionary key.
"""
    def __init__(self, *args, **kwargs):
        self._freeze()

    def __repr__(self):
        return 'frozen' + bitarray.__repr__(self)

    def __hash__(self):
        "Return hash(self)."
        if getattr(self, '_hash', None) is None:
            # ensure hash is independent of endianness, also the copy will be
            # mutable such that .tobytes() can zero out the pad bits
            a = bitarray(self, 'big')
            self._hash = hash((len(a), a.tobytes()))
        return self._hash

    # Technically the code below is not necessary, as all these methods will
    # raise a TypeError on read-only memory.  However, with a different error
    # message.
    def __delitem__(self, *args, **kwargs):
        ""  # no docstring
        raise TypeError("frozenbitarray is immutable")

    append = bytereverse = clear = extend = encode = fill = __delitem__
    frombytes = fromfile = insert = invert = pack = pop = __delitem__
    remove = reverse = setall = sort = __setitem__ = __delitem__
    __iadd__ = __iand__ = __imul__ = __ior__ = __ixor__ = __delitem__
    __ilshift__ = __irshift__ = __delitem__


def bits2bytes(__n):
    """bits2bytes(n, /) -> int

Return the number of bytes necessary to store n bits.
"""
    import sys
    if not isinstance(__n, (int, long) if sys.version_info[0] == 2 else int):
        raise TypeError("integer expected")
    if __n < 0:
        raise ValueError("non-negative integer expected")
    return (__n + 7) // 8


def test(verbosity=1, repeat=1):
    """test(verbosity=1, repeat=1) -> TextTestResult

Run self-test, and return unittest.runner.TextTestResult object.
"""
    from bitarray import test_bitarray
    return test_bitarray.run(verbosity=verbosity, repeat=repeat)
