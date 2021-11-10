import csv 

data1=[]
data2=[]

with open("data2.csv","r") as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        data1.append(row)

with open("data2.csv","r") as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        data2.append(row)

headers1=data1[0]
planet_data1=data1[1:]

headers2=data2[0]
planet_data2=data2[1:]

headers=headers1+headers2
planet_data=[]
for index,data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])


with open("final.csv","a+") as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)

