# Import Libraries
import txtimport
import timing

# Get Data
rdata = txtimport.text()
# Start the runtime timer
timing.start()

# Priorities Dict
priority = {
    
}

# Alphabet used to assign priority values
alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Assign priority values
i = 0
while i<len(alph):
    priority[alph[i]] = i+1
    i+=1

i=0
data = [[[],[],[]]]
# Parse out elf group data and assign groups of three
while i<len(rdata):
    
    blank = [[],[],[]]
    blank[0] = list(rdata[i])
    blank[1] = list(rdata[i+1])
    blank[2] = list(rdata[i+2])
    if i == 0:data[0] = blank
    else: data.append(blank)
    
    i+=3

# Look for common values
i=0
score = 0
while i<len(data):
    # Search for common points between elf groups
    j=0
    while j<len(data[i][0]):
        if data[i][1].count(data[i][0][j]) > 0 and data[i][2].count(data[i][0][j]) > 0:
            score += priority[data[i][0][j]]
            print(data[i][0][j])
            break
        j+=1

    i+=1
print(score)
