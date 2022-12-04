# Import Libraries
import txtimport
import timing

# Get Data
rdata = txtimport.text()
# Start the runtime timer
timing.start()

i=0
data=[]
while i<len(rdata):
    data.append(rdata[i].split(','))
    i+=1

i=0
while i<len(data):
    j = 0
    while j<len(data[i]):
        data[i][j] = data[i][j].split('-')
        j+=1
    i+=1

count = 0
i=0
print(data)
while i<len(data):
    if int(data[i][0][0]) <= int(data[i][1][1]) and int(data[i][0][1]) >= int(data[i][1][0]): count+=1
    
    i+=1
print(count)
timing.end()