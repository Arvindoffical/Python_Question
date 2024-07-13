#User function Template for python3
from typing import List
import heapq
from collections import defaultdict
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        # Create the graph as an adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        dist = [float('inf')] * (n + 1)
        dist[1] = 0
        
        # Min-heap to store (distance, vertex)
        heap = [(0, 1)]
        
        # To reconstruct the path
        parent = [-1] * (n + 1)

        while heap:
            current_dist, u = heapq.heappop(heap)

            # If we pop a node from the heap with a distance greater than the known shortest distance, skip it
            if current_dist > dist[u]:
                continue

            # Explore the neighbors
            for v, weight in graph[u]:
                distance = current_dist + weight

                
                if distance < dist[v]:
                    dist[v] = distance
                    parent[v] = u
                    heapq.heappush(heap, (distance, v))
        
        
        if dist[n] == float('inf'):
            return [-1]
        path = []
        node = n
        while node != -1:
            path.append(node)
            node = parent[node]
        path.reverse()
        return [dist[n]] + path
        # code here
        


#{ 
 # Driver Code Starts
from collections import defaultdict


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)

# } Driver Code Ends