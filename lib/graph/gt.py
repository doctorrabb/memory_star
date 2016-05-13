'''
    GTK interface module
'''

import pygtk
pygtk.require ('2.0')
import gtk
from lib.graph.eventsys import *


class MainWindow (object):

    def __init__ (self):
        '''
            This is a initialize of a Main Window on GTK interface.
            First block init's a window and it's size with position
        '''
        self.w = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.w.connect ('destroy', Events.WindowEvents.destr)
        self.w.set_position (gtk.WIN_POS_CENTER)
        self.w.set_size_request (1000, 800)
        self.w.set_title ('Memory Star')
        self.w.set_resizable (False)

        '''
            This block init's elements of our window.
        '''


        # 1. Initialize Exit Button
        self.exit_button = gtk.Button ('Exit')
        self.exit_button.connect ('clicked', Events.ButtonEvents.exit_button_func)

        # 2. Initialize Field with elements
        self.field = gtk.Fixed()
        self.field.put (self.exit_button, 10, 750)
        self.w.add (self.field)



        # Show the window and elements on it
        self.w.show_all ()

    def main (self):
        gtk.main ()
