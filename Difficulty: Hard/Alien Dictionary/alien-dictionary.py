#User function Template for python3

class Solution:
    def findOrder(self, dict, n, k):
        graph = {chr(i + 97): [] for i in range(k)}  # first k letters
        in_degree = {chr(i + 97): 0 for i in range(k)}

        for i in range(n - 1):
            min_len = min(len(dict[i]), len(dict[i + 1]))
            for j in range(min_len):
                if dict[i][j] != dict[i + 1][j]:
                    graph[dict[i][j]].append(dict[i + 1][j])
                    in_degree[dict[i + 1][j]] += 1
                    break
            else:
                if len(dict[i]) > len(dict[i + 1]):
                    return ""

        queue = [c for c in in_degree if in_degree[c] == 0]
        order = ""

        while queue:
            c = queue.pop(0)
            order += c
            for adj in graph[c]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)

        if len(order) != k:
            return ""

        return order
#{ 
 # Driver Code Starts
#Initial Template for Python 3


class sort_by_order:

    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

# } Driver Code Ends