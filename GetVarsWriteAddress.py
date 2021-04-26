#Returns the list of all variables that write to a specific address
#@author wagrenier
#@category Decompile
#@keybinding 
#@menupath 
#@toolbar 

# Import statements
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

# Setup variables related to the program
state = getState()
project = state.getProject()
currentProgram = state.getCurrentProgram()

refmanager = currentProgram.referenceManager

addr = currentProgram.getAddressFactory().getAddress('0x002e2208')

print(refmanager.getExternalReferences().hasNext())

for ref in refmanager.getReferencesTo(addr):
    ref2 = refmanager.getReferencesTo(ref)
    a = refmanager.getReferencedVariable(ref2[0])
    print(a)