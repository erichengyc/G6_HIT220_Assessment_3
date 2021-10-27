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

    def computeCosting(self, a, b):
    # unit costs for scanning all points on all paths between two locations and give exhaustive path for rangers to follow, returned as an list
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
    # return the point blocked eg A1 and the increase in protection provided using some weighting
        point="A1"
        protection=1
        return point, protection

    def minTime(self,a,b):
    #return list of points trevelled and the time required
        path=[]
        return path
        

    def findScope(self, a, b):
        #provide start and end point of search, collect points to consider in search
        pointList=[a,b]
          
        #find location of a and b in points list
        for index in range(0, size-1):
            if self.points[index ]== a:
                indexa=index
            if self.points[index] == b:
                indexb = index 
        #Find all paths a to b - Select direct routes only, no cycles or backtracking

        #Find shortest route from path options 

        # Add side points to inspect
        #include all nodes that are linked to (neighbour of) any internal point on path (ie point crocodiles can enter)  
        #       between a and b - this may add backtracking
        
        #Example findScope ("15","18")
            #paths are [15,16,18] and [15,16,17,19,20]
            #shortest path [15,16,18]
            #add neighbours [15,16,17,18]
        
        #This is the exhaustive list of points rangers need to inspect
        return pointList

if __name__ == '__main__':
   
    cm=CrocMonitor(size) 
    #print (cm.locationList)
    #Changed examples
    cm.computeCosting("15","18")
  
    # exhaustive path is  [15,16, 17,16, 18] so return the length of this as unit cost - note data changes in Locations.csv
    #algorithm to find scope of spanning tree is provided as findScope()
    cm.improveDistance("15","18")
    #output will be 16  Ratio is "original distance on [15,16,18]:0"
    cm.locateOptimalBlockage("15", "18")
    #returns 16 as other routes have alternative paths
    #may use other data to decide optimum path, but explain in requirements for this method
    cm.minTime("15", "18") 
    #returns [15,16,18] and time to travel that path