class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    
    
t = HashTable()
t['march 6'] = 120
t['march 6'] = 20
t['march 16'] = 10
t['march 10'] = 1200
t['march 172'] = 440
print(t['march 6'])
