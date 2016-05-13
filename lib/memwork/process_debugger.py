'''
    This is a main module. It was created for reading/writing data to/from process memory.
    © DOCTOR_RABB
'''


from ptrace.debugger import PtraceDebugger
import struct
from lib.memwork import data

class ProcessDebugger (object):

    def __init__(self, pid):
        self.debugger = PtraceDebugger ()
        self.process = self.debugger.addProcess (int (pid), False)
        self.addrs = list ()


    # TODO: Search's address in process memory by value.
    def search_addr_by_value (self, value):

        for i in self.process.readMappings():
            # Fuck, this is invalid bin :(
            if i.pathname in ['[vsyscall]', '[vdso]']:
                continue

            try:
                for j in i.search (value):
                    self.addrs.append (j)
            except:
                pass

        return self.addrs

    # TODO: Convert's boolean value to binary.
    def search_boolean_value (self, value):
        return self.search_addr_by_value (struct.pack (data.BIT_ENDOF + '?', value))

    # TODO: Convert's integer value to binary.
    def search_integer_value (self, value):
        return self.search_addr_by_value(struct.pack(data.BIT_ENDOF + 'i', value))
