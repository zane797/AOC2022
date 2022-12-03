# Import Libraries
import txtimport
import timing

# Get Data
data = txtimport.text()
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

# Parse out rucksack data into two compartments
while i<len(data):
    data[i] = list(data[i])
    midpoint = len(data[i])/2
    
    midpoint = int(midpoint)
    
    blank = [[],[]]
    blank[0] = data[i][:midpoint]
    blank[1] = data[i][midpoint:]
    data[i] = blank
    i+=1

# Look for common values
i=0
score = 0
print(data)
while i<len(data):
    # Search for common points between compartments
    j=0
    while j<len(data[i][0]):
        if data[i][1].count(data[i][0][j]) > 0:
            score += priority[data[i][0][j]]
            print(data[i][0][j])
            break
        j+=1

    i+=1
print(score)