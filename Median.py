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
newData.sort()

if n%2==0:
    median1=float(newData[n//2])
    median2=float(newData[(n//2)-1])
    median=(median1+median2)/2
else:
    median=newData[n//2]

print (median)
