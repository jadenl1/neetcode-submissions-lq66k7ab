class LRUCache:

    class Node:
        def __init__(self, key=None, val=None, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lruHead, self.lruTail = self.Node(), self.Node()
        self.lruHead.next, self.lruTail.prev = self.lruTail, self.lruHead

    def insert(self, newNode):
        # place right before tail
        prevNode = self.lruTail.prev
        prevNode.next = newNode
        newNode.prev = prevNode
        newNode.next = self.lruTail
        self.lruTail.prev = newNode

    def remove(self, node):
        nextNode = node.next
        prevNode = node.prev
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # update existing
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.insert(node)
        else:
            node = self.Node(key, value)
            self.insert(node)
            self.cache[key] = node
            # check capacity
            if len(self.cache) > self.capacity:
                head = self.lruHead.next
                self.remove(head)
                del self.cache[head.key]
