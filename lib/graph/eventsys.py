'''
    In this file we have events for GTK windows.
    © DOCTOR_RABB
'''

import pygtk
pygtk.require ('2.0')
import gtk

class Events (object):
    class WindowEvents (object):
        @classmethod
        def destr(self, widget, data=None):
            gtk.main_quit()

    class ButtonEvents (object):
        @classmethod
        def exit_button_func(self, widget):
            raise SystemExit(0)
