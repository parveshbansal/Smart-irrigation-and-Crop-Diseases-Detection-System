import operator
import math
import csv
import random
import datetime
import requests as r
#filename='E:\aavriti\Afsar Sir\Dataset.txt'
def loadDataset(filename,split,trainingSet=[], testSet=[]):
    with open(filename,'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(5):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

                
def euclideanDistance(instance1,instance2,length):
    distance = 0
    for x in range(length):
        distance+=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)




def getNeighbours(trainingSet, testInstance, k):
    distance=[]
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distance.append((trainingSet[x],dist))
    distance.sort(key=operator.itemgetter(1))
    neighbours=[]
    for x in range(k):
        neighbours.append(distance[x][0])
    return neighbours





def getResponse(neighbours):
    classVotes={}
    for x in range(len(neighbours)):
        response = neighbours[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response]=1
    sortedVotes = sorted(classVotes.items(),key=operator.itemgetter(1), reverse=True)#iteritems does not work in python 3
    return sortedVotes[0][0]




def main():
    #for sowing duration
    today = datetime.date.today()
    print(today)
    today=str(today)
    year=int(today[0:4])
    month=int(today[5:7])
    date1=int(today[8:10])
    #date of sowing
    res1=r.get('https://api.thingspeak.com/channels/814542/fields/2/last.json?api_key=GP5ITWB1ARGW7DHV&results=2')
    val1=res1.json()
    print(val1['field2'])
    k=val1['field2']
    month2=int(k[0:2])
    date2=int(k[3:5])
    year2=int(k[6:10])
    print(month2,date2,year2)
    a = datetime.date(year,month,date1)
    b = datetime.date(year2,month2,date2)
    datetime.timedelta(7)
    print((a-b).days)
    ###
    #Currently shown crop
    res1=r.get('https://api.thingspeak.com/channels/814542/fields/1/last.json?api_key=GP5ITWB1ARGW7DHV&results=2')
    val2=res1.json()
    shown=int(val2['field1'])
    print(shown)
    ####
    #current field condition
    res1=r.get('https://api.thingspeak.com/channels/816674/feeds/last.json?api_key=6JIRRMHSVNUTBHKT&results=2')
    val1=res1.json()
    temp=int(val1['field1'])
    moisture=int(val1['field2'])
    humidity=int(val1['field3'])
    res1=r.get('https://api.thingspeak.com/channels/814542/feeds/last.json?api_key=GP5ITWB1ARGW7DHV&results=2')
    val1=res1.json()
    typcrop=int(val1['field1'])
    print(temp,moisture,humidity)
    #####
    trainingSet=[]
    testSet=[]
    split = 0.67
    loadDataset(r'C:\Users\DELL\Desktop\dataset.txt',split,trainingSet,testSet)
    print('Train: '+repr(len(trainingSet)))
    print('Test: '+repr(len(testSet)))
    testInstance=[typcrop,shown,moisture,temp,humidity,]
    #testInstance=[2,32,700,32,32]
    prediction = []
    k=5
    neighbours = getNeighbours(trainingSet, testInstance, k)
    result = getResponse(neighbours)
    print(result)
    if(result=='1' and shown!=0):
       	s=r.get("msg service")
        print(s)
while True:
    main()
