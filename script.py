from random import *


def createGraph(size, expectedDegreeMin, expectedDegreeMax, maxDistance):
    graph = []
    targetDegree = (expectedDegreeMin + expectedDegreeMax) / 2
    nonZeroElementChance = targetDegree / size
    
    for i in range(size):
        graph.append([])
        for j in range(size):
            if (i == j):
                continue
            
            shouldBeNonZero = (random() < nonZeroElementChance)
            if(shouldBeNonZero):
                graph[i].append(int(uniform(0, maxDistance)))
            else:
                graph[i].append(0)
    return graph




def getGraphDegree(graph):
    totalDegree = 0
    size = len(graph)
    for row in graph:
        for element in row:
            if(element):
                totalDegree += 1
    
    return totalDegree / size
                





graph = createGraph(1200, 10, 100, 100)
# for row in graph:
#    print(row)



print(getGraphDegree(graph))