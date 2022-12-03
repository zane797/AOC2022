# Import Libraries
from typing import is_typeddict
import txtimport
import timing

# Get Data
data = txtimport.text()
# Start the runtime timer
timing.start()
dataref = []
i=0

# Parse the data to a new data array until 
while len(data) > 0:
    if data.count('') == 0: 
        dataref.append(data[0:])
        break
    dataref.append(data[:data.index('')])
    data = data[data.index('')+1:]
    i+=1

# Cycle through the data and convert all values to ints and add them up
i=0
while i<len(dataref):
    j=0
    value = 0
    while j<len(dataref[i]):
        value+=int(dataref[i][j])
        j+=1
    dataref[i] = value
    i+=1

# Find the sum of the three highest values
value = 0
i=0
while i<3:
    loc = dataref.index(max(dataref))
    value+=dataref[loc]
    dataref.pop(loc)
    i+=1
print(value)
# Finalize the runtime timer
timing.end()