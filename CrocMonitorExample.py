from typing import Sized
import csv

import math
import numpy as np
size=100
class CrocMonitor:
    locationList =[]
    import csv
    def __init__(self, size):
        
        self.locationList = []
        self.matrix = [[0 for x in range(size)]for y in range(size)]
        self.points=[]
        self.readData()
        self.storeDistance()

    def readData(self):
        with open('Locations.csv') as f:
            csv_reader = csv.reader(f)
            index = 0
            next(csv_reader)
            for line in csv_reader:
                
                pointName=line[0]
                x=line[1]
                y=line[2]
                number=line[3]
                edge=line[4]
                
                water=False
                if line[5] == "W":
                    water=True

                self.locationList .append( [pointName,  x, y, number, edge, water] ) # etc
                
                if not pointName in self.points:
                   
                    self.points.append(pointName)
                index += 1
        
        f.close()

    def storeDistance(self):
    
        for index in range(0, len(self.locationList)-1):
   
            if self.locationList[index][4]!="":
                startpoint = self.locationList[index][0]
                endpoint = self.locationList[index][4]
           
                for indexa in range (0, len(self.points)-1):
                    if self.points[indexa] == startpoint:
                        indexPointa=indexa
                
                        for indexb in range(0, len(self.points)-1):
                            if self.points[indexb] == endpoint:
                                indexPointb = indexb
                              
                                distance = self.computeDistance(startpoint, endpoint)
                           #store distance along path    
                                break
                        break
   
      

    def computePathDistance (self,a,b):
       
        #provide the distance between two points a and b on a paths. Assume not adjacent
        distance=0
        return distance
  

    def findPath(self,a,b):
        path=[]
        #returns shortest path a to b
        return path
        

    def computeDistance (self, a, b):
       
        # provide the distance between two points a and b on a path. Assume adjacent
        distance=0
        return distance

    def computeCosting(self, a, b):
    # unit costs for scanning between two locations and give path for rangers to follow, returned as an array
        path=[]
        costing=0
        return costing,path
    
    def improveDistance (self, a, b):
    #return point blocked as a value on map (eg A1) and scaled increase in distance between points
        point="A1"
        scaledImprovement=0
        return point, scaledImprovement

    def countCroc(self, beach, x):
    #count the number of crocs likely in a x mile radius of a beach. Return an array [location, number]
        number=0
        return number
            

    def locateOptimalBlockage(self,a,b):
    # return the point blocked eg A1 and the increase in protection provided using another weighting
        point="A1"
        protection=1
        return point, protection

    def minTime(self,a,b):
    #return array of points trevelled and the time required
        path=[]
        return path

if __name__ == '__main__':
   
    cm=CrocMonitor(size) 
    #print (cm.locationList)
    
    
    
    print(cm.locateOptimalBlockage("15","18"))
    #return 17 as other points have alternatives to bypass 
    cm.computeCosting("15","18")
    # minimal path is  [15,17,18] so return length of this as unit cost

    cm.locateOptimalBlockage("15", "18")
    #returns 17 as other routes have alternative paths
    #may use other data to decide optimum path, but explain in requirements for this method
