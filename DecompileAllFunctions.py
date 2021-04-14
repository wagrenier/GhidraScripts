#Script to export all functions to a file
#@author wagrenier
#@category Decompile
#@keybinding 
#@menupath 
#@toolbar 


def make_safe_filename(s):
    def safe_char(c):
        if c.isalnum():
            return c
        else:
            return "_"
    return "".join(safe_char(c) for c in s).rstrip("_")


# Import statements
import sys
import os
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

# Setup variables related to the program
state = getState()
project = state.getProject()
currentProgram = state.getCurrentProgram()
locator = project.getProjectData().getProjectLocator()
project_location = locator.getLocation()

# Load all functions defined in this program
fm = currentProgram.getFunctionManager()
funcs = fm.getFunctions(True) # True means 'forward'

# Setup variables related to the decompiler
ifc = DecompInterface()
ifc.openProgram(currentProgram)

# Check if output folder exists
try:
    os.mkdir('{}/Functions'.format(project_location))
except OSError:
    print ("Creation of the directory failed")
else:
    print ("Successfully created the directory")


# Decompile all functions
for func in funcs: 
    print('Decompiling function: {} @ 0x{}'.format(func.getName(), func.getEntryPoint()))
    try:
        results = ifc.decompileFunction(func, 0, ConsoleTaskMonitor())
        file_name = '{}/Functions/{}.cpp'.format(project_location, make_safe_filename(func.getName()))
        file = open(file_name, 'w')
        file.write(results.getDecompiledFunction().getC())
        file.close()
    except:
        e = sys.exc_info()[0]
        print('An error occured while trying to create the file {}, {}'.format(func.getName(), e))


