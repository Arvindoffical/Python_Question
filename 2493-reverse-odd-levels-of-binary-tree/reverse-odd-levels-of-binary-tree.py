from collections import deque

class Solution:
    def reverseOddLevels(self, root):
        lvl = 0
        q = deque([root])

        while q:
            size = len(q)
            nodes = []
            temp = deque(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                nodes.append(node.val)
            if lvl % 2 != 0:
                nodes.reverse()
                i = 0
                while size > 0:
                    node = temp.popleft()
                    node.val = nodes[i]
                    i += 1
                    size -= 1
            lvl += 1
        return root