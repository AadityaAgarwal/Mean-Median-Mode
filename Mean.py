import csv
with open('height.csv',newline='') as f:
    read=csv.reader(f)
    fileData=list(read)
    fileData.pop(0)

newData=[]

for i in range(len(fileData)):
    newList=fileData[i][2]
    newData.append(float(newList))

n=len(newData)
total=0

for x in newData:
    total+=x
mean=total/n
print(mean)
