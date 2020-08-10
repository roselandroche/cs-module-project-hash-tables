class LinkedList:
    def __init__(self):
        self.head = None
    
    def find(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def add_to_head(self, key, value):
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head
        if current.key == key:
            self.head = current.next
            return current
        previous = current
        current = current.next
        while current is not None:
            if current.key == key:
                previous.next = current.next
                return current
            else:
                previous = current
                current = current.next
        return None

    def insert_overwrite(self, key, value):
        node = self.find(value)
        if node is None:
            self.add_to_head(HashTableEntry(key, value))
        else:
            key.value = value

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.table = [ None ] * self.capacity
        self.stored_keys = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # number of stored keys divided by capacity
        return self.stored_keys / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash & 0xffffffff

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
        # Your code here
        # Grab Current Index
        index = self.hash_index(key)
        # Start of LL at index -> self.table[index]
        

        # Check to see if Storage[Index] is None
        # and Initiate LL
        if self.table[index] is None:
            self.table[index] = LinkedList()

        # Set Variable to current self.storage[index]
        # LL Reference
        ll_index = self.table[index]

        # If Head of LL is none, we have a virgin
        # LL List
        if ll_index is None:
            ll_index.add_to_head(key, value)
            self.stored_keys += 1

        # Check to see if key already exists
        # If key is found Update Value
        # Else Add To List
        else:
            found = ll_index.find(key)
            if found:
                found.value = value
            else:
                ll_index.add_to_head(key, value)
                self.stored_keys += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        found = None
        if self.table[index] is not None:
            found = self.table[index].find(key)
        if found:
            self.table[index].delete(key)
        else:
            print('Warning! Key not found.')
        return found

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        found = None
        if self.table[index] is not None:
            found = self.table[index].find(key)
        if found:
            return found.value
        return found

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # Make a new array thats DOUBLE the current size
        self.capacity = new_capacity
        old_table = self.table
        self.table = [ None ] * self.capacity
        # Go through each linked list in the array
        for item in old_table:
            if item is not None:
                current = item.head
                while current is not None:
                    key, value = current.key, current.value
                    # GO through each item and re-hash it
                    # Insert the items into their new locations
                    self.put(key, value)
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
