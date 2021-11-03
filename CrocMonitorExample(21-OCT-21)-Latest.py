from os import pathsep

from typing import Sized
import csv
import math
from collections import defaultdict, deque
import numpy as np

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
        for i in range(len(self.locationList)): 
            uniNode.add(self.locationList[i][0])  #add in the unique node in the uniNode 

        # g = Graph(len(uniNode))

        for x in range(len(self.locationList)):
            self.addEdge(str(self.locationList[x][0]), str(self.locationList[x][4]))        #call the addEdge function

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

    
    def addBilateralRelationship (self):
        # Add bilateral Neighbour relationship
        # For example, there is a record (17 with neighbour 20) in the original data file
        # The function add a new record (20 with neighbour 17)
        bilateralLocationList = []
        for location in self.locationList:  
            bilateralLocationList.append(location) 
        length = len(bilateralLocationList)
        index = 0
        for locationA in self.locationList:
            if index > length - 1:
                break
            for locationB in self.locationList:
                if locationA[4] == locationB[0]:
                    bilateralLocationList.append([locationB[0], locationB[1], locationB[2], locationB[3],locationA[0],locationB[5], locationA[6]])
                    break
            index += 1  
           
        return bilateralLocationList 
    
    
    
    
    def findScope(self, a, b):
        
        ### provide start and end point of search, collect points to consider in search
    
        pointList=[]
        # Add bilateral Neighbour relationship to find all possible paths
        # For example, there is a record (17 with neighbour 20) in the original data file
        # The function add a new record (20 with neighbour 17)
        bilateralLocationList = self.addBilateralRelationship()
              
        ### Find all paths a to b - Select direct routes only, no cycles or backtracking
        
        allPaths = []
        graph = defaultdict(list)
        uniNode = set()
        
        for i in range(len(bilateralLocationList)):
            uniNode.add(bilateralLocationList[i][0])
            
        for x in range(len(bilateralLocationList)):
            graph[str(bilateralLocationList[x][0])].append(bilateralLocationList[x][4])

        allPaths = self.findpaths(graph, a, b)
        print()
        print()
        print("Question 1 information: ")
        print("allPaths: ", allPaths)
        
        
        ##Find shortest route from path options 
        shortestPath = []
        shortestPathIndex = 0
        pathDistances = []
        # Get the distance of each path
        for index in range(len(allPaths)):
            pathDistance = self.computePathDistance(allPaths[index])
            pathDistances.append(pathDistance)
        
        # Get the smallest distance and find the index of the distance 
        # which is the same as the index where the shortest path is at   
        for index in range(len(pathDistances)):
            if pathDistances[index] == min(pathDistances):
                shortestPathIndex = index
                
        # Get the shortest path
        shortestPath = allPaths[shortestPathIndex]
           
        print('shortestPath: ', shortestPath)
 
        ## Add side points to inspect
        #include all nodes that are linked to (neighbour of) any internal point on path (ie point crocodiles can enter)  
        #       between a and b - this may add backtracking


        for point in shortestPath:
            pointList.append(point)
            
        internalPointAndNeighbours = []
        # Find the neighbours of internal points
        for location in bilateralLocationList:
            if location[0] in shortestPath[1:-1]:
                internalPointAndNeighbours.append([location[0], location[4]])
        # If the neighbour of an internal point is in any of the path options 
        # insert the neigbour into the point list at one position after the point    
        for internalPoint in internalPointAndNeighbours:
            for path in allPaths:
                if internalPoint[1] in path[1:-1] and internalPoint[1] not in pointList:
                    pointList.insert(pointList.index(internalPoint[0]) + 1, internalPoint[1])    
                  
        #Example findScope ("15","18")
            #paths are [15,16,18] and [15,16,17,19,20,18] 
            #shortest path [15,16,18]
            #add neighbours [15,16,17,18] (final result of the function)
        
        #This is the exhaustive list of points rangers need to inspect
        return pointList
    
    
    
    # Function to find the subset of an given element
    def getSubset(self, upper, i):
       if upper[i] == i:
            return i
       return self.getSubset(upper, upper[i])

    # Function to unify two subsets by rank
    def unifySubsets(self, upper, rank, set1, set2):
        set1root = self.getSubset(upper, set1)
        set2root = self.getSubset(upper, set2)

        # Put smaller rank tree under the root of high rank tree 
        if rank[set1root] < rank[set2root]:
            upper[set1root] = set2root
        elif rank[set1root] > rank[set2root]:
            upper[set2root] = set1root

        # If ranks are same, then make one as root and increment its rank by one
        else:
            upper[set2root] = set1root
            rank[set1root] += 1

    
    # Function to get the minimum spanning tree of a given graph
    def getMST(self, graph, numberOfVertices):

        
        minimumSpanningTree = []  
        
        # The index variable is used to access the graph edges
        indexa = 0

        # An index variable for the result list
        indexb = 0

        # Sort all the edges based on their weight (distance) in non-decreasing order
        graph = sorted(graph,
                            key=lambda item: item[2])

        upper = []
        rank = []

        # Create the number of vertices subsets
        for node in range( numberOfVertices):
            upper.append(node)
            rank.append(0)

        # The number of edges of a MST should be the 
        # number of graph vertices - 1
        while indexb <  numberOfVertices - 1:

            # Pick the shortest edge and increment the index 
            # by one for next iteration
            u, v, w = graph[indexa]
            indexa = indexa + 1
            x = self.getSubset(upper, u)
            y = self.getSubset(upper, v)

            # If the edge does not form a cycle, add it as part of the final MST 
            # otherwise the edge will be discarded 
            if x != y:
                indexb = indexb + 1
                minimumSpanningTree.append([u, v, w])
                self.unifySubsets(upper, rank, x, y)
            
        # The variable sotre the total weight (distance) of the final MST
        minimumCost = 0
        # Store all the vertices that the MST goes through
        exhaustivePath = []
        
       
        # Append all vertices went through and pring all edges with their distances
        for u, v, weight in minimumSpanningTree:
            minimumCost += weight
            exhaustivePath.append(u)
            exhaustivePath.append(v)
           
        return exhaustivePath,minimumCost
    
  
    
    
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
        exhaustivePath = []
        costing = 0
        
        pointList = []
        numOfVertices = 0
        graphEdges = []
        
        # Get the scope of the area betweem a and b
        pointList = self.findScope(a, b)
        print('pointList: ', pointList)
        # Get the number of vertices in the area graph
        numOfVertices = len(pointList)
        
        # Append graph edges     
        for point in pointList:
            for location in self.locationList:
                if point == location[0] and location[4] in pointList:
                    graphEdges.append([pointList.index(point), pointList.index(location[4]), location[6]])
        
        # Get the minimum spanning tree of the graph and the minimum weight (distance)
        results = []
        results = self.getMST(graphEdges, numOfVertices)
        costing = results[1]
       
        # Convert the indexs into actual locations 
        # and append them to the exhaustive path list
        for pointIndex in results[0]:
            exhaustivePath.append(pointList[pointIndex])
         
          
        print("The exhaustive path between two locations is: ", exhaustivePath) 
        # As the question states "cost is proportional to ground covered" 
        # the weight (distance) of the minimum spanning tree is returned as the minimum cost
        print("The minimum cost for performing an exhaustive search is: ", costing)  
        print()
        print()
        return costing, exhaustivePath

    #below function is a part of question 2
    def getPathforImproveDistance(self, a, b):
        bilateralLocationList = self.addBilateralRelationship()
        uniNode = set()  #create set of unique Node 
        for i in range(len(bilateralLocationList)): 
            uniNode.add(bilateralLocationList[i][0])  #add in the unique node in the uniNode 

        for x in range(len(bilateralLocationList)):
            self.addEdge(str(self.addBilateralRelationship()[x][0]), str(self.addBilateralRelationship()[x][4]))        #call the addEdge function

        return self.findpaths(self.graph, a, b)     #return to find path function

    #below function addresses the answer to question number 2
    def improveDistance(self, a, b):
        # this function returns point blocked as a value on map (eg A1) and scaled increase in distance between points
        
        #initialize variable
        path_distance = 0
        path_distance_sets = [] #used to store all possible paths between two points and their each path's distance 
        distance_list = [] #this list is used to store all the path distances to find the shortest path

        #find all possible paths
        all_paths = self.getPathforImproveDistance(a,b)
        
        #Calculate distances in all possible paths and store in path_distance_sets list to map which each path's distance.
        #path_distance_seets list will be used to get the shortest path using the shortest distance in coming steps
        for each_path in all_paths:
            path_distance = self.computePathDistance(each_path)

            path_distance_sets.append([each_path, path_distance])
            path_distance = 0

        #get all the distances in a seperate list called 'distance_list' to find the shortest distance
        for each_path_distance_set in path_distance_sets:
            distance_list.append(each_path_distance_set[1])

        #find the shortest distance using distance_list
        shortest_distance = min(distance_list)

        #find shortest path using the shortest distance calculated above
        for each_path_distance_set in path_distance_sets:
            if each_path_distance_set[1] == shortest_distance:
                shortest_path = each_path_distance_set[0]

        #Below explains how the optimum point to be blocked was decided and how the crocadile blocking situation was assumed
        #The point that will be blocked is the first neighbouring point for the source point on the shortest path, 
        # since this is the optimum place to block the croc on the shortest path.

        #For example is the cros were to go from "1" to "10a", the shortest path will be ['1', '2', '3', '4', '5', '6', '7', '9', '10a'] and 
        # the point blocked will be 2, because the first point croc travels from 1(source) is 2. So if that is blocked then 
        # the croc cannot travel any further on that shortest path and would have to take an alternative path. 
        # So the point cros goes to from the source point in the shortest path is the optimum blockage point
        
        # It is assumed the croc takes the second shortest path from '1' to '10a' as the alternative path.
        # So the seond shortest path distance is the new alternative distance.

        #Above logic is achieved from the below coding section and the shortest path calculated above

        #get the blocked point
        blocked_point = shortest_path[1] #as per the above explanation the optimum blocked point is the first point croc will go to from the source point
        
        #below section finds the new alternative distance
        
        #this if condition checks if there is only one possible path between the points. If there is only one possible path between two points then go to else section
        #if there are are 2 or more then new possible path will be found as below
        if len(path_distance_sets) > 1:

            #initialize variables
            new_possible_path_list = [] 
            new_possible_path_distance_sets = []
            new_distance_list = []
            count = 0

            #this for loop will create all the possible paths for the alternative path in new_possible_path_list.
            # the for loop will check if the second point in each path is the blocked point or not because 
            # if it is the blocked point then the crocodile cannot go in that path. Hence, not a possible alternative
            for each_path in all_paths:
                if each_path[1] != blocked_point:
                    new_possible_path_list.append(each_path)
                    path_distance = self.computePathDistance(each_path)

                    new_possible_path_distance_sets.append([each_path, path_distance])
                    path_distance = 0
                else:
                    #below count will make sure if all paths between two points are blocked using one blocked point or not
                    #example assume 15 to 18, there is only two possible paths: [15, 16, 18] and [15, 16, 17, 18]. Then blocking 16 on the 
                    # shortest path [15, 16, 18] would automatically block [15, 16, 17, 18] path too since 16 is blocked. (This example data,path are just for example purpose)

                    #so if count == number of all possible paths between two points then there is no alternative path after blocking the optimum point on shortest path
                    count += 1
            
            #print the blocked point
            print("Blocked point is:", blocked_point)
            
            #below if condition will check if the blocking point is present as second point in all paths. If so it will print the relevant
            #  output since there are no alternative paths since all paths are blocked by one point
            if count == len(all_paths):
                print("There is no alternative path since all the other possible paths also contains the blocked point. So the ratio is %d:0. Ratio in float cannot be calculated because any number devided by 0 is undefined. But the ratio of improvement is very large since the denominator is 0." %shortest_distance )
            else:
                #under the else section new alternative distance is calculated all over again as shown below by getting the second shortest distance

                #get all the distances in a seperate list called new_distance_list to find the second shortest distance
                #new_possible_path_distance_sets list contains all new possible paths after blocking the optimum point 
                for each_path_distance_set in new_possible_path_distance_sets:
                    new_distance_list.append(each_path_distance_set[1])

                #find the second shortest distance using the min funtion on the new_distance_list
                second_shortest_distance = min(new_distance_list)

                #find second shortest path using the second shortest distance calculated above
                for each_path_distance_set in new_possible_path_distance_sets:
                    if each_path_distance_set[1] == second_shortest_distance:
                        second_shortest_path = each_path_distance_set[0]

                #calculate ratio of improvement using the shortest distance and second shortest distance
                ratio_of_improvement = shortest_distance/second_shortest_distance

                #print the ratio
                print("Ratio is", shortest_distance, ":", second_shortest_distance,".","The ratio in float is", ratio_of_improvement)
        else:
            #there is only one possible path between the two points

            #There is no alternative path because there is only 1 possible path. So the croc has no other way of going to 
            # the destination when the shortest path which is the only path is blocked at the optimum point.
            second_shortest_distance = 0

            #The ratio_of_improvement is shortest_distance:0 because there is no alternative path.
            #but a integer/float cannot be devided by 0 due to zero devision error and any number deivded by 0 is undefined but a very large number. 
            #So the ratio of improvement in this case is very large. This explains the practical thinking as well since when there is only one path 
            # and that path is blocked then there is no way for croc to travel which makes a high improvement
            
            print("Blocked point is:", blocked_point)
            print("There is no alternative path since the only posible path is the shortest path. So the ratio is %d:0. Ratio in float cannot be calculated because any number devided by 0 is undefined. But the ratio of improvement is very large since the denominator is 0." %shortest_distance )

    def countCroc(self, beach, x):
    #count the number of crocs likely in a x mile radius of a beach. Return an array [location, number]

        num=0
        beaches = {}
        for x in range(len(self.locationList)):
            if self.locationList[x][0][0] == 'B':
                beaches[self.locationList[x][0]] = ([self.locationList[x][1],self.locationList[x][2]])  #ensure the node is equal to x and y axis 
        radius = [] #initial empty list for radius to save total distance of spots
        spot = self.locationList
        for i in beaches:
            a = i  #set it as a 
            for y in range(len(spot)):   #find the distance of each spot
                
                # to stop marking itself as a neighbour
                if spot[y][0]!= i:          #if spot is not equal to i
                    b = spot[y][0]          #then set b as every spot in list
                    distance = self.computeDistance(a,b)
                    radius.append([i,spot[y][0],distance])      #append the list of beach
        x = int(x)
        spotsinradius = []     #spots within radius of x
        for i in range(len(radius)):
            # if the iteration equals the beach user input
            if radius[i][0] == beach:   #if the value is equal to input value
                if radius[i][2] < x:  #if the radius of beach is < input value
                    spotsinradius.append(radius[i][1])         #append the spot list with radius 
        num = len(spotsinradius)    #count the number of radius of beach 
        return f'The number of crocodiles within {x}km of {beach} is {num}'

        return num,blocked

    def locateOptimalBlockage(self, a, b):
        # return the point blocked eg A1 and the increase in protection provided using some weighting

        point="A1"
        protection=1
        path=self.getPath(a,b)      #get the path the possible path
        nextpath=[]
        s1=a
        for x in range(0, len(self.locationList)-1):    
            if self.locationList[x][0]==s1:     #cros sighting is equal to a
                nextpath.append(s1)              #create add it in the new path list
                s1=self.locationList[x][4]      #s1 will euqal to neighbour
        for x in range(0, len(path)-1):         
            if path[x]!=nextpath[x]:         #if the path value is not equal to the new path value  
                point=path[x-1]                 #point equal to step back 1 path value
                break                               
        return point, protection                    
    

    def minTime(self, a, b):
        print("Loop 2") 
        # return list of points trevelled and the time required
        paths = self.getPath(a, b)      #get the all the possible paths
        print(paths)

        min_time = 0        #initial minimum time
        min_path = []       #initial minimum path list

        for path in paths: 
            index = paths.index(path)   #returns the index path
            pathTime = 0   
            print("Loop 2") 
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


    


if __name__ == '__main__':

    cm = CrocMonitor(size)
    ### All functions are commented out, please run them individually when testing each question

    # Question 1
    #cm.computeCosting("15", "18")
    # exhaustive path is  [15,16, 17,16, 18] so return the length of this as unit cost - note data changes in Locations.csv
    
    # Question 2
    # algorithm to find scope of spanning tree is provided as findScope()
    #print(cm.improveDistance("15", "18"))
    # output will be 16  Ratio is "original distance on [15,16,18]:0"
    
    # Question 3
    #print(cm.locateOptimalBlockage("15", "18"))
    #print(cm.countCroc("B5", 16))
    
    # returns 16 as other routes have alternative paths
    # may use other data to decide optimum path, but explain in requirements for this method
    #print(cm.minTime("1", "10a"))
    # returns [15,16,18] and time to travel that path
