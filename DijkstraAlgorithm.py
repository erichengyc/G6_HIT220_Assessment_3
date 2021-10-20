from typing import Sized
import csv
import math
import numpy as np
import heapq

size=100

class CrocMonitor:
    locationList =[]
    def __init__(self, size):
        
        self.locationList = []
        self.matrix = [[0 for x in range(size)]for y in range(size)]
        self.points=[]
        self.readData()
        self.storeDistance()
        self.visited = False
        # this is the node where we came from in the shortest path
        self.predecessor = None
        # this is how we store the children (edges will represent the neighbors)
        self.adjacency_list = []
        # this is the minimum distance (shortest path) from the source vertex (starting vertex)
        self.min_distance = float('inf')

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

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

    def computeDistance (self, a, b):
       
        # provide the distance between two points a and b on a path. Assume adjacent
        distance=0
        # distance = math.sqrt((int(a[1])-int(b[1]))**2 + (int(a[2])-int(b[2]))**2)
        return distance




class DijkstraAlgorithm:

    def __init__(self):
        # this is the heap representation (binary heap and not Fibonacci heap)
        self.heap = []

    def calculate(self, startpoint):

        # initialize the vertices
        startpoint.min_distance = 0
        heapq.heappush(self.heap, startpoint)

        # have to iterate until the heap is not empty
        while self.heap:

            # we pop the vertex with lowest min_distance parameter
            # pop function removes the given item !!!
            actual_vertex = heapq.heappop(self.heap)

            if actual_vertex.visited:
                continue

            # we have to consider the neighbors
            for edge in actual_vertex.adjacency_list:
                u = edge.startpoint
                v = edge.endpoint
                # we have to compare the min_distances
                new_distance = u.min_distance + edge.weight

                # there is a shorter path to the v vertex
                if new_distance < v.min_distance:
                    # when there is a shortest path available then we update the
                    # predecessor accordingly
                    v.predecessor = u
                    v.min_distance = new_distance
                    # update the heap - this is the lazy implementation
                    # WHY? Because it takes O(N) to find the vertex we want to update (v)
                    # plus we have O(logN) to handle the heap again [O(N)+O(logN)=O(N)]
                    # Fibonacci heaps - O(1)
                    heapq.heappush(self.heap, v)

            actual_vertex.visited = True

    @staticmethod
    def get_shortest_path(vertex):

        print("Shortest path to vertex %s is: %s" % (vertex.pointName, str(vertex.min_distance)))

        actual_vertex = vertex

        while actual_vertex is not None:
            print("%s " % actual_vertex.pointName)
            actual_vertex = actual_vertex.predecessor


if __name__ == "__main__":

    cm=CrocMonitor(size) 
    print(cm.locationList)

    for i in range(0,len(cm.locationList)):
        print(cm.locationList[i])

    # create the vertices (nodes)
    # node1 = Node("A")
    # node2 = Node("B")
    # node3 = Node("C")
    # node4 = Node("D")
    # node5 = Node("E")
    # node6 = Node("F")
    # node7 = Node("G")
    # node8 = Node("H")

    # create the edges (directed edges)
    # edge1 = Edge(5, node1, node2)
    # edge2 = Edge(8, node1, node8)
    # edge3 = Edge(9, node1, node5)
    # edge4 = Edge(15, node2, node4)
    # edge5 = Edge(12, node2, node3)
    # edge6 = Edge(4, node2, node8)
    # edge7 = Edge(7, node8, node3)
    # edge8 = Edge(6, node8, node6)
    # edge9 = Edge(5, node5, node8)
    # edge10 = Edge(4, node5, node6)
    # edge11 = Edge(20, node5, node7)
    # edge12 = Edge(1, node6, node3)
    # edge13 = Edge(13, node6, node7)
    # edge14 = Edge(3, node3, node4)
    # edge15 = Edge(11, node3, node7)
    # edge16 = Edge(9, node4, node7)

    # handle the neighbors
    # node1.adjacency_list.append(edge1)
    # node1.adjacency_list.append(edge2)
    # node1.adjacency_list.append(edge3)
    # node2.adjacency_list.append(edge4)
    # node2.adjacency_list.append(edge5)
    # node2.adjacency_list.append(edge6)
    # node8.adjacency_list.append(edge7)
    # node8.adjacency_list.append(edge8)
    # node5.adjacency_list.append(edge9)
    # node5.adjacency_list.append(edge10)
    # node5.adjacency_list.append(edge11)
    # node6.adjacency_list.append(edge12)
    # node6.adjacency_list.append(edge13)
    # node3.adjacency_list.append(edge14)
    # node3.adjacency_list.append(edge15)
    # node4.adjacency_list.append(edge16)

    # we just have to run the application
    algorithm = DijkstraAlgorithm()
    algorithm.calculate(cm.locationList[0])
    # algorithm.get_shortest_path(node7)
