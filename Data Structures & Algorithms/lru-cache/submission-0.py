class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node, order by recency
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def remove(self, node):
        # remove LRU key (update ptrs to remove element at beginning of cache)
        prv = node.prev 
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv

    def add(self, node):
        # add key-val pair to end of cache (head.next)
        prv, nxt = self.head, self.head.next
        prv.next = nxt.prev = node
        node.next, node.prev = nxt, prv


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        if len(self.cache) > self.capacity:
            # remove from cache (update ptrs)
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
