from typing import Sized
import csv
import math
from collections import defaultdict, deque

# import numpy as np
size = 100

class CrocMonitor:
    locationList = []
    import csv
    def __init__(self, size):

        self.locationList = []
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.points = []
        self.readData()
        self.storeDistance()
        self.graph = defaultdict(list)

    def readData(self):
        with open('Locations.csv') as f:
            csv_reader = csv.reader(f)
            index = 0
            next(csv_reader)
            for line in csv_reader:

                pointName = line[0]
                x = line[1]
                y = line[2]
                number = line[3]
                edge = line[4]

                water = False
                if line[5] == "W":
                    water = True

                self.locationList.append([pointName, x, y, number, edge, water])  # etc

                if not pointName in self.points:
                    self.points.append(pointName)
                index += 1

        f.close()

    def storeDistance(self):

        # Iterates through the location list and get the index at each location
        for index in range(0, len(self.locationList) - 1):
            # Check if the neighbor column is null at current location row
            if self.locationList[index][4] != "":
                # If not null, assign the current location to be the start point of the edge
                startpoint = self.locationList[index][0]
                # Assign the neighbor of the start point to be the end point
                endpoint = self.locationList[index][4]
                # Calculate the distance between the start and end points   
                distance = self.computeDistance(startpoint, endpoint)
                # Append the distance to the last column of the location row
                self.locationList[index].append(distance)
        return

    def computePathDistance(self, path):

        # provide the distance between two points a and b, as the end points on a path. Assume not adjacent
        distance = 0
        for node in range(len(path)):
            try:
                distance += self.computeDistance(path[node], path[node+1])
            except:
                pass
        return distance


    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Utility function to check if current
    # vertex is already present in path
    def isNotVisited(self, x, path):
        size = len(path)
        for i in range(size):
            if (path[i] == x):
                return 0
        return 1

    # Utility function for finding paths in graph
    # from source to destination
    def findpaths(self, g, src, dst) -> None:

        # Create a queue which stores
        # the paths
        q = deque()

        # Path vector to store the current path
        allPath = []
        path = []
        path.append(src)
        q.append(path.copy())

        while q:
            path = q.popleft()
            last = path[len(path) - 1]

            # If last vertex is the desired destination
            # then print the path
            if (last == dst):
                allPath.append(path)

            # Traverse to all the nodes connected to
            # current vertex and push new path to queue
            for i in range(len(g[last])):
                if (self.isNotVisited(g[last][i], path)):
                    newpath = path.copy()
                    newpath.append(g[last][i])
                    q.append(newpath)
        return allPath

    def getPath(self, a, b):
        uniNode = set()
        for i in range(len(cm.locationList)):
            uniNode.add(cm.locationList[i][0])

        # g = Graph(len(uniNode))

        for x in range(len(cm.locationList)):
            self.addEdge(str(cm.locationList[x][0]), str(cm.locationList[x][4]))

        return self.findpaths(self.graph, a, b)




    def computeDistance(self, a, b):

        # provide the distance between two points a and b on a path. Assume adjacent

        # Initialize the distance and the x, y coordinates of location a and b
        distance = 0
        xA = 0
        xB = 0
        yA = 0
        yB = 0
        # Find x, y coordinates of location a and b
        for location in self.locationList:
            if location[0] == a:
                xA = location[1]
                yA = location[2]
            if location[0] == b:
                xB = location[1]
                yB = location[2]
        # Calculate the distance between location a and b      
        distance = math.sqrt((int(xA) - int(xB)) ** 2 + (int(yA) - int(yB)) ** 2)
        return distance

    def computeCosting(self, a, b):
        # unit costs for scanning all points on all paths between two locations and give exhaustive path for rangers to follow, returned as an list
        path = []
        costing = 0
        return costing, path

    def improveDistance(self, a, b):
        # return point blocked as a value on map (eg A1) and scaled increase in distance between points
        point = "A1"
        scaledImprovement = 0
        return point, scaledImprovement

    def countCroc(self, beach, x):
        # count the number of crocs likely in a x mile radius of a beach. Return an array [location, number]
        number = 0
        return number

    def locateOptimalBlockage(self, a, b):
        # return the point blocked eg A1 and the increase in protection provided using some weighting
        point = "A1"
        protection = 1
        return point, protection

    def minTime(self, a, b):
        # return list of points trevelled and the time required
        path = self.getPath(a, b)

        for eachPath in path:
            distance = self.computePathDistance(eachPath)
            print(distance)


    def findScope(self, a, b):
        # provide start and end point of search, collect points to consider in search
        pointList = [a, b]

        # find location of a and b in points list
        for index in range(0, size - 1):
            if self.points[index] == a:
                indexa = index
            if self.points[index] == b:
                indexb = index
                # Find all paths a to b - Select direct routes only, no cycles or backtracking

        # Find shortest route from path options

        # Add side points to inspect
        # include all nodes that are linked to (neighbour of) any internal point on path (ie point crocodiles can enter)
        #       between a and b - this may add backtracking

        # Example findScope ("15","18")
        # paths are [15,16,18] and [15,16,17,19,20]
        # shortest path [15,16,18]
        # add neighbours [15,16,17,18]

        # This is the exhaustive list of points rangers need to inspect
        return pointList


if __name__ == '__main__':

    cm = CrocMonitor(size)
    # print (cm.locationList)

    for i in range(0, len(cm.locationList)):
        print(cm.locationList[i])

    # Changed examples
    cm.computeCosting("15", "18")

    # exhaustive path is  [15,16, 17,16, 18] so return the length of this as unit cost - note data changes in Locations.csv
    # algorithm to find scope of spanning tree is provided as findScope()
    cm.improveDistance("15", "18")
    # output will be 16  Ratio is "original distance on [15,16,18]:0"
    cm.locateOptimalBlockage("15", "18")
    # returns 16 as other routes have alternative paths
    # may use other data to decide optimum path, but explain in requirements for this method
    cm.minTime("1", "10a")
    # returns [15,16,18] and time to travel that path
