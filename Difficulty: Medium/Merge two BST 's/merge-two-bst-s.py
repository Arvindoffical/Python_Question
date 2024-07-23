#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def merge(self, root1, root2):
        # code here
        def convert(n):
            if not n or (not n.left and not n.right):
                return n

            if n.left:
                l = convert(n.left)
                l.is_threaded = True
                l.right = n

            if not n.right:
                return n

            return convert(n.right)

        def left_most(n):
            while n and n.left:
                n = n.left

            return n

        def next(n):
            if getattr(n, 'is_threaded', False):
                n = n.right

            else:
                n = left_most(n.right)

            return n
            
        convert(root1) 
        convert(root2)

        c1, c2 = left_most(root1), left_most(root2)

        ans = []

        while c1 and c2:

            if c1.data < c2.data:

                ans.append(c1.data)

                c1 = next(c1)

            else:

                ans.append(c2.data)

                c2 = next(c2)

        while c1:
            ans.append(c1.data)

            c1 = next(c1)

        while c2:
            ans.append(c2.data)

            c2 = next(c2)

        return sorted(ans)        # code here

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == 'N':
        return None
    
    # Creating list of strings from input string after splitting by space
    ip = s.split()
    
    # Create the root of the tree
    root = Node(int(ip[0]))
    
    # Push the root to the queue
    queue = [root]
    
    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        currNode = queue.pop(0)
        
        # Get the current node's value from the string
        currVal = ip[i]
        
        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.left)
        
        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.right)
        i += 1
    
    return root



def main():
    t = int(input())
    for _ in range(t):
        s = input()
        root1 = buildTree(s)
        s = input()
        root2 = buildTree(s)
        obj = Solution()
        vec = obj.merge(root1, root2)
        print(" ".join(map(str, vec)))

if __name__ == "__main__":
    main()

# } Driver Code Ends