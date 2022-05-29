class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
        self.nextMin = None


class MinStack(object):

    def __init__(self):
        self.head = None
        # TODO: Use priority queue here.
        self.minNode = None

        self.minHead = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head == None:
            self.head = Node(val, None, None)
            self.minNode = self.head
            return

        newNode = Node(val, None, self.head)
        self.head.prev = newNode
        self.head = newNode

        if val < self.minNode.value:
            if self.minNode != None:
                newNode.nextMin = self.minNode
            self.minNode = newNode

    def pop(self):
        """
        :rtype: None
        """
        re_val = self.head
        self.head = self.head.next
        if self.head != None:
            self.head.prev = None

        if re_val == self.minNode:
            self.minNode = re_val.nextMin

        return re_val.value

    def top(self):
        """
        :rtype: int
        """
        return self.head.value

    def getMin(self):
        """
        :rtype: int
        """
        return self.minNode.value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
