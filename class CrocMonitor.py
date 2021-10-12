class CrocMonitor:

    import numpy as np
    import csv
    def __init__(self, name, age):
        #choose which one you want
        self.locationList = []
        self.locationList=np.array ([])

    def readData(self):
        with open('Locations.csv') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                pointName=line[0]
                #etc
        f.close()
    
    def computeDistance (self, a, b):
        # provide the distance between two points a and b on the paths. They may not be adjacent
        
   
    def computeCosting(self, a, b):
    # unit costs for scanning between two locations and give path for rangers to to follow, returned as an array
    
    def improveDistance (self, a, b):
    #return edge blocked as a duple (c,d) and scalled increase in distance between points

    def countCroc(self, beach):
    #count the number of crocs likely in a 10 mile radius of a beach. Return an array of locations and numbers


    def locateOptimalBlockage(self,a,b):
    # return the edge blocked and the increase in protection provided using another weighting

    def minTime(self,a,b):
    #return array of points trevelled and the time required
