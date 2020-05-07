class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity=2, storage=None, counter=0):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.counter = counter
        self.load = self.counter / self.capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

        prime = 1099511628211
        hash = 14695981039346656037

        for i in key:           
            hash = hash * prime
            hash = hash ^ ord(i)
        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash_value = 5381
        for byte in key.encode('utf-8'):
            hash_value = ((hash_value * 33) + hash_value) + byte # hash * 33 + byte
        return hash_value

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        pos = self.storage[index]        

        if self.load > 0.7:
            self.resize(self.capacity * 2)

        if pos is None:
            self.storage[index] = HashTableEntry(key, value)
            return

        prev = pos
        
        while pos is not None:
            if pos.key == key:
                pos.value = value
                return 

            prev = pos
            pos = pos.next

        self.counter += 1
        prev.next = HashTableEntry(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        cur = self.storage[index]
        prev = None

        while cur is not None and cur.key != key:
            prev = cur
            cur = cur.next

        if cur is None:
            return None
        else:
            self.counter -= 1
            if prev is None:
                self.storage[index] = cur.next
            else:
                prev.next = prev.next.next
            return

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        pos = self.storage[index]

        while pos is not None:
            if pos.key == key:
                return pos.value
            
            pos = pos.next

        if pos is None:
            return None
        else:
            return pos.value                   

    def len(self):
        return self.counter

    def resize(self, capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        #if (self.counter / self.capacity) > 0.7:
        # print(capacity)
        # if capacity is not None:
        #     self.capacity = capacity
        #     self.storage = [None] * self.capacity
        # else:
        print(capacity)
        cur_hash = self.storage
        self.capacity = capacity
        self.storage = [None] * capacity

        for item in cur_hash:
            if item is not None:
                # print(item.key, item.value)
                while item is not None:
                    self.put(item.key, item.value)
                    item = item.next

        # print(self.capacity)
        # if self.load < .2:
        #     cur_hash = self.storage
        #     self.capacity = self.capacity // 2
        #     self.storage = [None] * self.capacity * 2

        #     for item in cur_hash:
        #         if item is not None:
        #             while item is not None:
        #                 self.put(item.key, item.value)
        #                 item = item.next

        return


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")
    ht.put("line_4", "Tiny hash table")
    ht.put("line_5", "Filled beyond capacity")
    ht.put("line_6", "Linked list saves the day!")
    ht.put("line_7", "Tiny hash table")
    ht.put("line_8", "Linked list saves the day!")
    ht.put("line_9", "Tiny hash table")
    
    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")

    print(ht.len())