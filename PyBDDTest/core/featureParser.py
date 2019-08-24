import os
import glob
import re
from pprint import pprint

patterns ={
    "Feature":r"^Feature",
    "Scenario":r"Scenario",
    "Given":r"Given",
    "When":r"When",
    "Then":r"Then",
    "And":r"And",
    "But":r"But"
}

ListOfFiles =[]
for name in glob.glob('Features/*.feature'):
    ListOfFiles.append(name)

# print (ListOfFiles)

LineOfFeatures =[]

Data ={
"Feature" :[],
"Scenario" : [],
"Given" : [],
"When" : [],
"Then" :[],
"And" : []
}
with open(ListOfFiles[0],"r") as featureFile:
    for line in featureFile.readlines():
        line = line.strip()
        for key,pat in patterns.items():
            if re.match(pat,line):
                Data[key].append(line)

        LineOfFeatures.append(line)

# print (LineOfFeatures[0:20])

pprint (Data)