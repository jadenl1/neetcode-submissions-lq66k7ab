class LRUCache:
    class Node:
        def __init__(self, key, val, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.cacheMap = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        result = -1
        if key in self.cacheMap:
            node = self.cacheMap[key]
            result = node.val
            # remove node
            if node != self.tail:
                if node == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                # move to tail
                node.prev = self.tail
                node.next = None
                self.tail.next = node
                self.tail = node
        
        return result

    def put(self, key: int, value: int) -> None:
        node = self.Node(key, value)
        if not self.head:
            self.head = node
            self.tail = node
            self.cacheMap[key] = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            # remove old node if not new
            if key in self.cacheMap:
                oldNode = self.cacheMap[key]
                if oldNode != self.tail:
                    if oldNode == self.head:
                        self.head = self.head.next
                        self.head.prev = None
                    else:
                        oldNode.prev.next = oldNode.next
                        oldNode.next.prev = oldNode.prev

            self.cacheMap[key] = node

            # now check if we have reached capacity
            if len(self.cacheMap) > self.capacity:
                # remove head
                del self.cacheMap[self.head.key]
                self.head = self.head.next
                if self.head != None:
                    self.head.prev = None

