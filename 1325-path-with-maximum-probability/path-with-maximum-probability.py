#Python3 Code
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {i: {} for i in range(n)}

        
        for i, (u, v) in enumerate(edges):
            prob = succProb[i]
            graph[u][v] = prob
            graph[v][u] = prob

        max_heap = [(-1, start_node)] 
        probs = [0] * n
        probs[start_node] = 1

        while max_heap:
            
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob  

            if curr_prob < probs[node]:
                continue

            for neighbor, edge_prob in graph[node].items():
                new_prob = curr_prob * edge_prob
                if new_prob > probs[neighbor]:
                    probs[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))  

        return probs[end_node]