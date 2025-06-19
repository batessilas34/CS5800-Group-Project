# Group Project #1
# Sujith Peddireddy
# Silas Bates
# Dhruv Kansara
# Krishna Inapurapu


from collections import defaultdict
from typing import List
import random
import heapq
import time

def networkDelayTime(times, n, k):
    """
    :type times: List[List[int]]
    :type n: int
    :type k: int
    :rtype: int
    """
    # Initializing the priority queue
    pq = []
    # Initializing a dictionary to traverse each node   
    graph = defaultdict(list)

    # Creating a graph from the times array
    for source, destination, weight in times:
        graph[source].append((destination, weight))
    # Initializing distance and previous arrays
    distance = []
    previous = []
    visited = []

    # Setting the distance to each node to ~infinity and 
    # Setting the previous node to null for each node
    # Setting each visited node to False
    for i in range(n):
        distance.append(90000000000000)
        previous.append(None)
        visited.append(False)
    # Setting the source node distance to 0
    distance[k-1] = 0

    # Pushing the source node onto the queue
    heapq.heappush(pq, k)
    # Iterating over the entire graph
    while len(pq) != 0:
        # Poping the next node in the queue and setting visited to true
        source = heapq.heappop(pq)
        visited[source - 1] = True

        # Dijkstra's Algorithm
        for destination, weight in graph[source]:
            if visited[destination - 1] == False:
                if distance[destination - 1] > distance[source - 1] + weight:
                    distance[destination - 1] = distance[source - 1] + weight
                    previous[destination - 1] = source
                    heapq.heappush(pq, destination)

    # Determining if all nodes were visited
    all_nodes = 0
    for i in range(len(visited)):
        if visited[i] == False:
            all_nodes = 1
        
    # If a node was unreachable return -1
    # if all nodes were reached return the max distance
    # from Dijkstra's algorithm
    if all_nodes == 1:
        return -1
    else:
        return max(distance)


# Function to create a random array of edges and weights given a number
# of nodes. 
def create_graph(n):
    graph = []

    for i in range(n):
        edge = [i, random.randint(0,n), random.randint(10,200)]
        graph.append(edge)
    
    return graph


def main():

    # Example problem from LeetCode
    example_graph = [[2,1,1], [2,3,1], [3,4,1]]
    minimum_time = networkDelayTime(example_graph, 4, 2)
    print("Worked Example")
    print("n = 4")
    print("k = 2")
    print("times = [[2,1,1], [2,3,1], [3,4,1]]")
    print("Minimum Network Delay = " + str(minimum_time))


    # Empiracal timing data gathering
    n = 200
    while n < 500000:
        runtimes = []
        for x in range(20):
            graph = create_graph(n)
            start_time = time.perf_counter()
            minimum_time = networkDelayTime(graph, n, 1)
            stop_time = time.perf_counter()
            runtime = stop_time - start_time
            runtimes.append(runtime)
        print("n: " + str(n) + " runtime: " + str(sum(runtimes) / len(runtimes)))
        n = 2 * n




if __name__ == "__main__":
    main()
