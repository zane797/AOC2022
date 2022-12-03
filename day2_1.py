# Import Libraries
import txtimport
import timing

# Get Data
data = txtimport.text()
# Start the runtime timer
timing.start()

i=0
score=0
while i<len(data):
    temp = data[i].split(' ')
    # Challenger chooses Rock
    if temp[0] == 'A':
        if temp[1] == 'X':
            score+=4
        elif temp[1] == 'Y':
            score+=8
        elif temp[1] == 'Z':
            score+=3
    # Challenger chooses Paper
    if temp[0] == 'B':
        if temp[1] == 'X':
            score+=1
        elif temp[1] == 'Y':
            score+=5
        elif temp[1] == 'Z':
            score+=9
    # Challenger chooses Scissors
    if temp[0] == 'C':
        if temp[1] == 'X':
            score+=7
        elif temp[1] == 'Y':
            score+=2
        elif temp[1] == 'Z':
            score+=6
    i+=1
print(score)
# Finalize the runtime timer
timing.end()