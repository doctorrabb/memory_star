from optparse import OptionParser
from lib.graph import gt

def main ():
    op = OptionParser ('-G <pid>')
    op.add_option ('-G', '--graph', default=False, action='store_true', dest='graph', help='if you want to use GTK interface use this option')
    (op, args) = op.parse_args ()

    if op.graph:
        window = gt.MainWindow ()
        window.main ()

if __name__ == '__main__': main ()