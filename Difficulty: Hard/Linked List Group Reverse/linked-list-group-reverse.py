"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        l = []
        i = 0
        t = []
        while head:
            t.append(head.data)
            head = head.next
            i += 1
            if i == k or not head:
                l.append(t)
                t = []
                i = 0
        n = []
        for i in range(len(l)):
            n.extend(reversed(l[i]))
        # print(n)
        
        new = Node(n[0])
        current = new
        for i in range(1,len(n)):
            t = Node(n[i])
            current.next = t
            current = current.next
        
        return new
#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())  # Number of test cases
    while t > 0:
        llist = LinkedList()

        # Read list values and push them to the LinkedList
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)

        k = int(input())  # Size of the group for reversal
        ob = Solution()
        new_head = ob.reverseKGroup(llist.head, k)
        llist.head = new_head
        llist.printList()  # Print the modified linked list
        t -= 1

        print("~")

# } Driver Code Ends