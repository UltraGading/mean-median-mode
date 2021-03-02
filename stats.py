import csv
from collections import Counter 
with open('SOCR-HeightWeight2.csv', newline= '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))
def mean():
    n = len(new_data)
    total = 0
    for x in new_data:
        total += x
    mean = total/n
    print(str(mean))
def median():
    n = len(new_data)
    if n % 2 == 0:
	    median1 = float(new_data[n//2])
	    median2 = float(new_data[n//2 - 1])
	    median = (median1 + median2)/2
    else:
	    median = new_data[n//2]
    print("Median is: " + str(median))
def mode():
    data=Counter(new_data)
    modedataforrange = {"50-60":0,"60-70":0,"70-80":0}
    for height,occurence in data.items() :
        if 50<float(height)<60:
            modedataforrange["50-60"]+=occurence
        elif 60<float(height)<70:
            modedataforrange["60-70"]+=occurence
        elif 70<float(height)<80:
            modedataforrange["70-80"]+=occurence
    moderange,modeoccurence = 0,0
    for range,occurence in modedataforrange.items():
        if occurence>modeoccurence:
            moderange,modeoccurence = [int(range.split("-")[0]),int(range.split("-")[2])],occurence
    mode = float((moderange[0]+moderange[2])/2)
    print(mode)            
mean()
median()
mode()