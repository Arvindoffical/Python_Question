#User function Template for python3

class Solution:
    def minTime(self, root, target):
        from collections import deque
        def find_target_and_map_parents(node, parent, parent_map):
            if not node:
                return None
            if node.data == target:
                self.target_node = node
            parent_map[node] = parent
            find_target_and_map_parents(node.left, node, parent_map)
            find_target_and_map_parents(node.right, node, parent_map)
        parent_map = {}
        self.target_node = None
        find_target_and_map_parents(root, None, parent_map)
        queue = deque([(self.target_node, 0)])
        visited = set()
        max_time = 0
        
        while queue:
            node, time = queue.popleft()
            visited.add(node)
            max_time = max(max_time, time)
            if node.left and node.left not in visited:
                queue.append((node.left, time + 1))
            if node.right and node.right not in visited:
                queue.append((node.right, time + 1))
    
            parent = parent_map[node]
            if parent and parent not in visited:
                queue.append((parent, time + 1))
        
        return max_time


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends