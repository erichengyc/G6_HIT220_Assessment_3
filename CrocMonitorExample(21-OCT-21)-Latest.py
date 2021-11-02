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


    def addEdge(self, u, v):
        self.graph[u].append(v)     #add the edges between start point and end point

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
        uniNode = set()  #create set of unique Node 
        for i in range(len(cm.locationList)): 
            uniNode.add(cm.locationList[i][0])  #add in the unique node in the uniNode 

        # g = Graph(len(uniNode))

        for x in range(len(cm.locationList)):
            self.addEdge(str(cm.locationList[x][0]), str(cm.locationList[x][4]))        #call the addEdge function

        return self.findpaths(self.graph, a, b)     #return to find path function 

    def computePathDistance(self, path):

        # provide the distance between two points a and b, as the end points on a path. Assume not adjacent
        distance = 0        #initial distance as 0
        for node in range(len(path)):  
            try:            #calculate the compute distance from start point to destination point
                distance += self.computeDistance(path[node], path[node+1])
            except:
                pass
        return distance

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

    #below function addresses the answer to question number 2
    def improveDistance(self, a, b):
        # this function returns point blocked as a value on map (eg A1) and scaled increase in distance between points
        path_distance = 0
        path_distance_sets = []
        distance_list = []

        #find all possible paths
        all_paths = self.getPath(a,b)
        
        #calculate distances in all possible paths and store in path_distance list to map which pat has
        #  the shortest and second shortest distance in coming steps
        for each_path in all_paths:
            path_distance = self.computePathDistance(each_path)

            path_distance_sets.append([each_path, path_distance])
            path_distance = 0

        #using the path_distance list get all the distances in a seperate list to find the shortest distance
        for each_path_distance_set in path_distance_sets:
            distance_list.append(each_path_distance_set[1])

        #find the shortest distance using distance_list
        shortest_distance = min(distance_list)

        #find shortest path using the shortest distance calculated above
        for each_path_distance_set in path_distance_sets:
            if each_path_distance_set[1] == shortest_distance:
                shortest_path = each_path_distance_set[0]

        #Below explains how the optimum point to be blocked was decided and how the crocadile blocking situation was assumed
        #The point that will be blocked is the first neighbouring point for the source point 
        # on the shortest path since this is the optimum place to block the croc on the shortest path
        #Fr example is the cros were to go from "1" to "10a", the shortest path will be ['1', '2', '3', '4', '5', '6', '7', '9', '10a'] and 
        # the point blocked will be 2, because the first point croc travels from 1(source) is 2. So if that is blocked then 
        # the croc cannot travel travel any further on that shortest path and would have to take the second shortest path from '1' to '10a'.
        # So the seond shortest path is the new alternative distance.

        #Above logic is achieved from the below coding section and the shortest path calculated above

        #get the blocked point
        blocked_point = shortest_path[1] #as per the above explanation the optimum blocked point is the first point croc will go to from the source point
        if len(path_distance_sets) != 1:
            #calculate new alternative distance
            distance_list.remove(shortest_distance)
            second_shortest_distance = min(distance_list)

            #find second shortest path using the second shortest distance calculated above
            for each_path_distance_set in path_distance_sets:
                if each_path_distance_set[1] == second_shortest_distance:
                    new_alternative_path = each_path_distance_set[0]

            ratio_of_improvement = shortest_distance/second_shortest_distance
            print("Blocked point is:", blocked_point)
            print("Ratio is", shortest_distance, ":", second_shortest_distance,".","The ratio in float is", ratio_of_improvement)
        else:
            #There is no alternative path because there is only 1 possible path. So the croc has no other way of going to 
            # the destination when the shortest path which is the only path is blocked at the optimum point.
            second_shortest_distance = 0

            #The ratio_of_improvement is shortest_distance:0 because there is no alternative path.
            #but a integer/float cannot be devided by 0 due to zero devision error and any number deivded by 0 is undefined but a very large number. 
            #So the ratio of improvement in this case is veery large. This explains the practical thinking as well since when there is only one path 
            # and that path is blocked then there is no way for croc to travel which makes a hich improvement
            
            print("Blocked point is:", blocked_point)
            print("There is no alternative path since the only posible path is the shortest path. So the ratio is %d:0. Ratio in float cannot be calculated because any number devided by 0 is undefined. But the ratio of improvement is very large since the denominator is 0." %shortest_distance )

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
        paths = self.getPath(a, b)      #get the all the possible paths
        print(paths)

        min_time = 0        #initial minimum time
        min_path = []       #initial minimum path list

        for path in paths: 
            index = paths.index(path)   #returns the index path
            pathTime = 0    
            for node in range(len(path)):
                try:
                    distance = self.computeDistance(path[node], path[node+1])   #calculate the start point to destination point
                    for location in self.locationList:
                        if location[0] == path[node]:       #if crocs sight equal to node
                            if location[4] == path[node+1]:     #if neighbor is the destination point 
                                if location[5] is True:         #if route is water 
                                    pathTime += distance / 16   #find the speed when it's in water
                                elif location[5] is False:      #elif route is land
                                    pathTime += distance / 6    #fidn the speed when it's on land
                except:
                    pass

            if index == 0:     
                min_time = pathTime  #min time equal path time
                min_path = path     #min path equal to path
            else:               #this is to get the mininum time from start point to destination
                if pathTime < min_time:     #if path Time is smaller than min time
                    min_time = pathTime     #min time equal to path 
                    min_path = path         #min path equal to path

        print(min_time, min_path)


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
