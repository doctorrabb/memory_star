'''
   This is a main data file. Here we have information about size of types and "binary start".
   © DOCTOR_RABB
'''

import struct
import sys

BIT_ENDOF = ''

# Let's detect user's byteorder.
if sys.byteorder == 'little': BIT_ENDOF = '<'
else: BIT_ENDOF = '>'

# Class with types size.
class SizeInfo (object):
    boolean = struct.calcsize ('b')
    integer = struct.calcsize ('i')
    float = struct.calcsize ('f')
    double = struct.calcsize ('d')
    void = struct.calcsize ('P')
