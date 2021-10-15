'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        loopNode = self.identifyLoopNode(head)
        if (loopNode is not None):
            numberOfLoopNodes = self.identifyNumberOfNodesInLoop(loopNode)
            self.removeEdge(head, numberOfLoopNodes)
        # curHead = head
        # while(curHead is not None):
        #     print(curHead.data)
        #     curHead = curHead.next

    def removeEdge(self, head, numberOfLoopNodes):
        forwardHead = head
        k = 0 
        while (k<numberOfLoopNodes):
            forwardHead = forwardHead.next
            k += 1
        while (head != forwardHead):
            head = head.next
            forwardHead = forwardHead.next
        # forwardHead = forwardHead
        while (forwardHead.next != head):
            forwardHead = forwardHead.next
        forwardHead.next = None
        
    def identifyNumberOfNodesInLoop(self, loopNode):
        curLoopNode = loopNode
        k = 1
        while (curLoopNode.next != loopNode):
            curLoopNode = curLoopNode.next
            k  += 1
        return k
    """
     This method might not work if there's no loop
    """
    def identifyLoopNode(self, head):
        fast = head.next
        slow = head
        while (fast is not None and fast.next is not None and slow is not None and fast != slow):
            fast = fast.next.next
            slow = slow.next
        if fast is None or fast.next is None:
            return None
        else:
            return fast


#{ 
#  Driver Code Starts
# driver code:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,num):
        if self.head is None:
            self.head=Node(num)
            self.tail=self.head
        else:
            self.tail.next=Node(num)
            self.tail=self.tail.next
    
    def isLoop(self):
        if self.head is None:
            return False
        
        fast=self.head.next
        slow=self.head
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast=fast.next.next
            slow=slow.next
        
        return True
    
    def loopHere(self,position):
        if position==0:
            return
        
        walk=self.head
        for _ in range(1,position):
            walk=walk.next
        self.tail.next=walk
    
    def length(self):
        walk=self.head
        ret=0
        while walk:
            ret+=1
            walk=walk.next
        return ret

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=tuple(int(x) for x in input().split())
        pos=int(input())
        
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)
        
        Solution().removeLoop(ll.head)
        
        if ll.isLoop() or ll.length()!=n:
            print(0)
            continue
        else:
            print(1)

# } Driver Code Ends