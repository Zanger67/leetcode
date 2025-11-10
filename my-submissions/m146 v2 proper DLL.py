class DLLNode:
    def __init__(
        self,
        key: int,
        data: int,
        prev_node: Optional['DLLNode'] = None,
        next_node: Optional['DLLNode'] = None
    ):
        self.key = key
        self.data = data
        self.prev = prev_node
        self.next = next_node

class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.key2node = {}
        self.cap = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.key2node :
            return -1

        output_data = self.pop(key)
        self.append_end(key, output_data)
        return output_data

    def put(self, key: int, value: int) -> None:
        if key in self.key2node :
            self.pop(key)

        if self.size >= self.cap :
            self.pop()

        self.append_end(key, value)

    def append_end(self, key: int, data: int) -> None:
        new_node = DLLNode(key=key, data=data, prev_node=self.tail)
        self.key2node[key] = new_node
        self.size += 1

        # this should apply to both if tail and head doesn't exist
        # since if at least one node exists, it's both tail and head
        if not self.tail :
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    # Default pop last
    def pop(self, key: int = None) -> int :
        if self.size == 0 :
            return -1

        # Pop LFU node by default
        if key is None :
            key = self.head.key

        if key not in self.key2node :
            return -1

        self.size -= 1
        popping_node = self.key2node.pop(key)
        output_data = popping_node.data

        # If it was the only node in DLL
        if self.size == 0 :
            self.head = None
            self.tail = None
            return output_data

        # if is head
        if popping_node.prev is None :
            self.head = popping_node.next
            if self.head is not None :
                self.head.prev = None
            return output_data

        # if is tail
        if popping_node.next is None :
            self.tail = popping_node.prev
            if self.tail is not None :
                self.tail.next = None
            return output_data

        # Regular node
        prev_node, next_node = popping_node.prev, popping_node.next
        prev_node.next, next_node.prev = next_node, prev_node
        return output_data


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)