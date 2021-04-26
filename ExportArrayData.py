# Takes an array and exports it as a defined python dictionnary where the key is the address
#@author wagrenier
#@category DataExport
#@keybinding 
#@menupath 
#@toolbar 


# Import statements
import json
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

# Setup variables related to the program
state = getState()
project = state.getProject()
currentProgram = state.getCurrentProgram()


def ExportArrayData(address, data_size, array_size, filename): 
    curr_address = int(address, 16)
    dic = {}

    for index in range(0, array_size):
        addr = currentProgram.getAddressFactory().getAddress(hex(curr_address))
        data_bytes = bytearray(getBytes(addr, data_size))

        num = 0x0
        for i in range(0, len(data_bytes)):
            num |= (data_bytes[i] << (i * 8))
    
        dic[hex(curr_address)] = num
        curr_address += data_size

    file = open(filename, 'w')
    file.write(json.dumps(dic))
    file.close


ExportArrayData('0x002f30b8', 0x4, 12609, 'C:\Users\willi\\cd_dat_tbl.json')