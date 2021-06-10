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
    '75-85':0,
    '85-95':0,
    '95-105':0,
    '105-115':0,
    '115-125':0,
    '125-135':0,
    '135-145':0,
    '145-155':0,
    '155-165':0,
    '165-175':0
}

for h,occurance in data.items():
    if 75<float(h)<85:
        mode['75-85']+=occurance
    elif 85<float(h)<95:
        mode['85-95']+=occurance
    elif 95<float(h)<105:
        mode['95-105']+=occurance
    elif 115<float(h)<125:
         mode['115-125']+=occurance
    elif 125<float(h)<135:
         mode['125-135']+=occurance
    elif 135<float(h)<145:
         mode['135-145']+=occurance
    elif 145<float(h)<155:
         mode['145-155']+=occurance
    elif 155<float(h)<165:
         mode['155-165']+=occurance
    elif 165<float(h)<175:
         mode['165-175']+=occurance
modeRange,modeOccurance=0,0

for range,occurance in mode.items():
    if occurance>modeOccurance:
        modeRange,modeOccurance=[int(range.split('-')[0]),int(range.split('-')[1])],occurance

finalMode=float((modeRange[0]+modeRange[1])/2)
print(finalMode)
