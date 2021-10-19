# Question 3 	 

# You are again asked to find the minimum distance between two locations in terms of number of metres 
# and hence time for croc to travel. Croc speed is about 16 km/hr in water and 6km/hr on land. You are 
# required to specify the route in terms of the points travelled through on the path. Method minTime() 
# returns an array and a time value 

# As an extension, provide the number of crocs in a certain radius of a beach. Using this array of 
# locations, decide which is the optimum path segment between two points to insert a blockage 
# that would  make the beach safer, by increasing the time the maximum number of crocs would 
# have to travel. 


import csv
with open('Locations.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)

    count = 0
    fsa = []

    for row in reader:
        count += 1
        # print(row[0])
        fsa.append(row[0])
        # if count > 10: 
        #     break
print(fsa)


import numpy as np
import csv

class CrocMonitor:
    
    def __init__(self, name, age):
        #choose which one you want
        self.locationList = []
        self.locationList=np.array ([])

    def readData(self):
        with open('Locations.csv') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                Croc_sightings=line[0]
                x=line[1]
                y=line[2]
                num_season = line[3]
                neighbours= line[4]
                Water_land_route = line[5]
                self.locationList[0] = [Croc_sightings, x, y,num_season, neighbours, Water_land_route ]
        f.close()

print("CrocMonitor.locationList[0]", CrocMonitor.locationList[0])


# if __name__ == '__main__':
#     locationList[0]
    
    # def computeDistance (self, a, b):
    #     # provide the distance between two points a and b on the paths. They may not be adjacent
   
    # def computeCosting(self, a, b):
    # # unit costs for scanning between two locations and give path for rangers to to follow, returned as an array
    
    # def improveDistance (self, a, b):
    # #return edge blocked as a duple (c,d) and scalled increase in distance between points

    # def countCroc(self, beach):
    # #count the number of crocs likely in a 10 mile radius of a beach. Return an array of locations and numbers


    # def locateOptimalBlockage(self,a,b):
    # # return the edge blocked and the increase in protection provided using another weighting

    # def minTime(self,a,b):
    # #return array of points trevelled and the time required














# References:
# CSV Column To Python List - https://youtu.be/4mqyi8Vqk78

#to find min time with dijkstra
# https://stackoverflow.com/questions/11835883/how-to-calculate-minimum-time-of-travel-between-two-places-when-a-matrix-contain