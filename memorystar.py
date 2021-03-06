# coding: utf8


'''
    This is a main file. Run it, please ;)
    © DOCTOR_RABB
'''

from optparse import OptionParser
try:
    from lib.graph import gt
except ImportError: 
    print 'For using GTK install PyGTK!'
    
from sys import argv, exit as ex

from lib.memwork.process_debugger import ProcessDebugger

def main ():
    
    if len (argv) < 4:
        print 'Use: memeorystar.py <value> <type> <pid>'
        ex (-1)
    
    op = OptionParser ('memorystar.py <value> <type> <pid>')
    op.add_option ('-G', '--graph', default=False, action='store_true', dest='graph', help='if you want to use GTK interface use this option')
    (op, args) = op.parse_args ()

    if op.graph:
        window = gt.MainWindow ()
        window.main ()
    else:
        dbg = ProcessDebugger (argv [-1])
        if argv [-2] == 'boolean': print dbg.search_boolean_value (argv [-3])
        elif argv [-2] == 'integer': print dbg.search_integer_value (argv [-3])
        else: print dbg.search_addr_by_value (argv [-3])

if __name__ == '__main__': main ()
