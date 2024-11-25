class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for _ in range(self.max)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
        
    def add_item(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))
    
    def get_item(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        return None
    
    def delete(self,key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h],[idx]
                return True
        return False
        
    def get_all_keys(self):
        keys =[]
        for buck in self.arr:
            for key, val in buck:
                keys.append(key)
        return keys
        
        
ht = HashTable()
ht.add_item('hat', 12)
ht.add_item('cow', 22)
ht.add_item('car', 43)
ht.add_item('jug', 64)

print(ht.get_item("jug"))
print(ht.get_all_keys())
