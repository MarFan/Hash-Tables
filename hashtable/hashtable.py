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
    def __init__(self, storage, capacity=2):
        self.capacity = capacity
        self.storage = [None] * capacity

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

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # index = self.hash_index(key)      
        # self.storage[index] = HashTableEntry(key, value)

        index = self.hash_index(key)
        if self.storage[index] is not None:
            for n in self.storage[index]:
                if n[0] == key:
                    n[1] = value
            else:
                self.storage[index].append([key, value])
            
        else:
            self.storage[index] = []
            self.storage[index].append([key, value])


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is not None:
            self.storage[index] = None
        else:
            print('index not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            return None
        else:
            for n in self.storage[index]:
                if n[0] == key:
                    return n[1]
            return None
        # if self.storage[index] is not None:
        #     for kvp in self.storage[index]:
        #         if kvp[0] == key:
        #             kvp[1] = value
        #             break
        #         else:
        #             self.storage[index].append([key, value])
        #     return self.storage[index].value
        # else:
        #     self.storage[index] = []
        #     self.storage[index].append([key, value])
            

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

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
