import csv
from collections import Counter
with open('height.csv',newline='') as f:
    read=csv.reader(f)
    fileData=list(read)
    fileData.pop(0)

newData=[]

for i in range(len(fileData)):
    newList=fileData[i][2]
    newData.append(float(newList))
data=Counter(newData)
mode={
    '50-60':0,
    '60-70':0,
    '70-80':0,
}

for h,occurance in data.items():
    if 50<float(h)<60:
        mode['50-60']+=occurance
    elif 60<float(h)<70:
        mode['60-70']+=occurance
    elif 70<float(h)<80:
        mode['70-80']+=occurance

modeRange,modeOccurance=0,0

for range,occurance in mode.items():
    if occurance>modeOccurance:
        modeRange,modeOccurance=[int(range.split('-')[0]),int(range.split('-')[1])],occurance

finalMode=float((modeRange[0]+modeRange[1])/2)
print(finalMode)
