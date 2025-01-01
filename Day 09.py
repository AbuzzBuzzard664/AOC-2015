
from itertools import permutations

def GetPuzzleInput():
    places = set()
    graph = {}
    with open("input09.txt") as file:
        for line in file:
            startcity, _, endcity, _, distance = line.strip().split()
            places.add(startcity)
            places.add(endcity)
            if startcity not in graph:
                graph[startcity] = {}
            if endcity not in graph:
                graph[endcity] = {}
            graph[startcity][endcity] = int(distance)
            graph[endcity][startcity] = int(distance)
    return places, graph

places, graph = GetPuzzleInput()
shortest = float('inf')
longest = 0
for perm in permutations(places):
    dist = 0
    for i in range(len(perm)-1):
        dist += graph[perm[i]][perm[i+1]]
    shortest = min(dist, shortest)
    longest = max(dist, longest)

print(shortest)
print(longest)