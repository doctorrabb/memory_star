import struct
import sys

BIT_ENDOF = ''

if sys.byteorder == 'little': BIT_ENDOF = '<'
else: BIT_ENDOF = '>'

class SizeInfo (object):
    boolean = struct.calcsize ('b')
    integer = struct.calcsize ('i')
    float = struct.calcsize ('f')
    double = struct.calcsize ('d')
    void = struct.calcsize ('P')