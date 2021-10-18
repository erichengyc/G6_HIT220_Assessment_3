from typing import Sized
import csv
import math
import numpy as np

size=100
class CrocMonitor:
    locationList =[]
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

                self.locationList.append( [pointName,  x, y, number, edge, water] ) # etc
                
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
   
      

    def computePathDistance (self,path):
       
        #provide the distance between two points a and b, as the end points on a path. Assume not adjacent
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

    def computeCosting(self, a, b): #Kevin
    # unit costs for scanning all points on all paths between two locations and give exhaustive path for rangers to follow, returned as an list
        path=[]
        costing=0
        return costing,path
    
    def improveDistance (self, a, b): #Melisha
    #return point blocked as a value on map (eg A1) and scaled increase in distance between points
        point="A1"
        scaledImprovement=0
        return point, scaledImprovement

    def countCroc(self, beach, x): #Eric 
    #count the number of crocs likely in a x mile radius of a beach. Return an array [location, number]
        number=0
        return number
            

    def locateOptimalBlockage(self,a,b): #Eric
    # return the point blocked eg A1 and the increase in protection provided using some weighting
        point="A1"
        protection=1
        return point, protection

    def minTime(self,a,b): #Eric
    #return list of points trevelled and the time required
        path=[]
        return path

if __name__ == '__main__':
   
    cm=CrocMonitor(size) 
    print (cm.locationList[0])
    
    
    
    print(cm.locateOptimalBlockage("15","18"))
    #return 17 as other points have alternatives to bypass 
    cm.computeCosting("15","18")
    # exhaustive path is  [15,16, 17,16, 18] so return length of this as unit cost - note data changes in Locations.csv

    cm.locateOptimalBlockage("15", "18")
    #returns 16 as other routes have alternative paths
    #may use other data to decide optimum path, but explain in requirements for this method
