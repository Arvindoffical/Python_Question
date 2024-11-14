# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = {}

        # get subtree's heights by dfs
        def get_height(node):
            if not node:
                return -1
            if node in heights:
                return heights[node.val]
            
            height = 1 + max(get_height(node.left), get_height(node.right))
            heights[node.val] = height
            return height
        get_height(root)

        # bfs approach:
        # on each level, find two subtrees with the largest heights, h1 >= h2
        # each node on the same level is being cut.
        # if node.val = h1, max_height = depth + h2, else depth + h1
        # h1, h2 = -1, -1 at initialisation since a null child implies a step back to parent
        max_heights = {root.val: 0}
        queue = deque([root])
        depth = 0
        while queue:
            k = len(queue)
            # get first and second max heights
            h1, h2 = -1, -1
            for i in range(k):
                h = heights[queue[i].val]
                if h > h1:
                    h1, h2 = h, h1
                elif h > h2:
                    h2 = h
            while k:
                k -= 1
                node = queue.popleft()
                h = heights[node.val]
                if h == h1:
                    max_heights[node.val] = h2 + depth
                else:
                    max_heights[node.val] = h1 + depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
            
        return [max_heights[q] for q in queries]