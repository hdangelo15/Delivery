# Hash Table class that will store the package data

class PackageHashTable:
    # hash table constructor
    def __init__(self, initial_size=10):
        self.table = []
        for i in range(initial_size):
            self.table.append([])

    # gets the hash key
    def get_hash(self, key):
        package_hash = key % len(self.table)
        return package_hash

    # finds a package in the hash table using the key
    def search(self, key):
        search_hash = self.get_hash(key)
        for kv_pair in self.table[search_hash]:
            if kv_pair[0] == key:
                return kv_pair[1]

    # inserts a package into the hash table
    def insert(self, key, value):
        insert_hash = self.get_hash(key)
        self.table[insert_hash].append([key, value])

    # updates a package in the hash table
    def update(self, key, value):
        update_hash = self.get_hash(key)
        for kv_pair in self.table[update_hash]:
            if kv_pair[0] == key:
                kv_pair[1] = value

    # deletes a package from the hash table
    def delete(self, key):
        delete_hash = self.get_hash(key)
        for index, kv_pair in enumerate(self.table[delete_hash]):
            if kv_pair[0] == key:
                del self.table[delete_hash][index]

