# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        def dfs(node):
            if not node: return []
            if not node.left and not node.right: return [1]
            left, right = dfs(node.left), dfs(node.right)
  
            for l in left:
                if right and l + right[0] > distance: break
                for r in right:
                    if l + r > distance: break
                    self.result += 1

            # merge sort left and right
            merged = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    val = left[l] + 1
                    l += 1
                else:
                    val = right[r] + 1
                    r += 1
                if val > distance:
                    break
                merged.append(val)

            while l < len(left) and left[l] + 1 < distance:
                merged.append(left[l] + 1)
                l += 1
            while r < len(right) and right[r] + 1 < distance:
                merged.append(right[r] + 1)
                r += 1
            return merged
        
        dfs(root)
        return self.result
        