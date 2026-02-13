# Linear Data Structures
# 021 Lab: Build a Hash Table

class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, string: str) -> int:
        output = 0
        for charact in string:
            output += ord(charact)
        return output
    
    def add(self, key: str, value: str) -> None:
        key_hash = self.hash(key)
        # if two different keys produce the same hash, the second one replaces the first ( no duplicates in dict ): create a bucket to handle collision
        if key_hash not in self.collection:
            # self.collection[key_hash] = {key: value} --> così sovrascrivi sempre, anche quando il bucket non esiste
            self.collection[key_hash] = {} # se il bucket non esiste, crealo
        self.collection[key_hash][key] = value
    
    def remove(self, key):
        key_hash = self.hash(key)
        if key_hash in self.collection and key in self.collection[key_hash]:
            del self.collection[key_hash][key]

    def lookup(self, key) -> str:
        key_hash = self.hash(key)
        if key_hash in self.collection and key in self.collection[key_hash]:
            return self.collection[key_hash][key]
        else: return None

    def __str__(self):
        return f'{self.collection}'

my_table = HashTable()
print(my_table.hash('golf'))
my_table.add('golf', 'sport')
my_table.add('dear', 'friend')
my_table.add('read', 'book')
print(my_table)
my_table.remove('dear')
print(my_table)
print(my_table.lookup('golf'))
