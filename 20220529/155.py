
class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class MinStack(object):

    def __init__(self):
        self.head = None
        self.minNode = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head == None:
            self.head = Node(val, None, None)

        newNode = Node(val, None, self.head)
        self.head.prev = newNode
        self.head = newNode



    def pop(self):
        """
        :rtype: None
        """
        re_val = self.head
        self.head = self.head.next
        return re_val
        

    def top(self):
        """
        :rtype: int
        """
        return self.head
        

    def getMin(self):
        return self.minNode
        """
        :rtype: int
        """


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
