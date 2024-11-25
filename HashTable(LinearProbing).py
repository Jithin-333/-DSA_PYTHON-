class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [None for x in range(self.max)]
        self.size = 0
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
        
    def add_item(self,key,value):
        if self.size / self.max > 0.7:
            self.rehash()
        h = self.get_hash(key)
        while self.arr[h] is not None:
            h = (h +1) % self.max
        self.arr[h] = (key,value)
        self.size += 1
    
    def get_item(self, key):
        h = self.get_hash(key)
        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                return self.arr[h][1]
            h = (h+1) % self.max
        return False
        
    def delete_item(self,key):
        h = self.get_hash(key)
        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                self.arr[h] = None
                self.size -= 1
                return True
            h = (h+1)%self.max
        return False
                
        
    def rehash(self):
        old_arr = self.arr
        self.max *= 2
        self.arr = [None for x in range(self.max)]
        self.size = 0
        for item in old_arr:
            if item is not None:
                self.add_item(item[0],item[1])
        
        
        
        
hash = HashTable()
