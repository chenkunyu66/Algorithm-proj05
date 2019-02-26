#cse 331
#kunyu Chen
#project05

class HashMap:
    def __init__(self, load_factor=0.75):
        # You may change the default maximum load factor
        self.max_load_factor = load_factor
        # Other initialization code can go here
        self._capacity = 20
        self._length = 0
        self.items = [[] for i in range(self._capacity)]

#This funciton is to get the number of the items in the map
    def __len__(self):
        return self._length

#This function is to get the load of the map
    def load(self):
        return self._length/self._capacity

#a bool function which is to check whether key is in the map
    def __contains__(self, key):
        index = self.hash_fun(key)
        if self.items[index]:
            for ele in self.items[index]:
                if self.equals(key, ele[0]):
                    return True
        return False

#get in the index of the key 
    def __getitem__(self, key):
        index = self.hash_fun(key)
        if self.items[index]:
            for ele in self.items[index]:
                if self.equals(key, ele[0]):
                    return ele[1]
        raise KeyError(key)

    def set_no_resize(self,key,value):
        index = self.hash_fun(key)
        if self.items[index]:
            for ele in self.items[index]:
                if self.equals(key, ele[0]):
                    self.items[index].remove(ele)
                    break

        self.items[index].append((key, value))
        

 #adding key and value into the map by resize function       
    def __setitem__(self, key, value):
        index = self.hash_fun(key)
        if self.items[index]:
            for ele in self.items[index]:
                if self.equals(key, ele[0]):
                    self.items[index].remove(ele)
                    self._length -= 1
                    break

        self.items[index].append((key, value))
        self._length += 1
        #check if the load is too large
        if self.load()>self.max_load_factor:
            self.resize()
        return True

 #adding key and value into the map by resize function   
    def __delitem__(self, key):
        index = self.hash_fun(key)
        if self.items[index]:
            for ele in self.items[index]:
                if self.equals(key, ele[0]):
                    self.items[index].remove(ele)
                    self._length -= 1
                    #check if the load is too small
                    if self.load()<0.05:
                        self.resizeHalf()
                    return True
        else:
            raise KeyError(key)

        
#get (key,value)
    def __iter__(self):
        ret = []
        for item in self.items:
            if item:
                for ele in item:
                    ret.append(ele)
        return iter(ret)

#clear everything in the map
    def clear(self):
        self.__init__()

    def keys(self):
        kset = []
        for item in self.items:
            if item:
                for ele in item:
                    kset.append(ele[0])
        return set(kset)

    # supplied methods

    def __repr__(self):
        return '{{{0}}}'.format(','.join('{0}:{1}'.format(k, v) for k, v in self))

    def __bool__(self):
        return not self.is_empty()

    def is_empty(self):
        return len(self) == 0

    # Helper functions can go here

#resizing the map when the size of map is too big
    def resize(self):
        old_list=self.items
        self._capacity= self._capacity*2
        self.items = [[] for i in range(self._capacity)]
        for list1 in old_list:
            if list1 is not None:
                for ele in list1:
                    if ele is not None:
                        self.set_no_resize(ele[0],ele[1])
        return True

#resizing the map when the size of map is too small
    def resizeHalf(self):
        old_list=self.items
        self._capacity= int(self._capacity/2)
        self.items = [[] for i in range(self._capacity)]
        for list1 in old_list:
            if list1 is not None:
                for ele in list1:
                    if ele is not None:
                        self.set_no_resize(ele[0],ele[1])
        return True

    def hash_fun(self, key):
        index = 5381

        if type(key) == str:
            for item in key:
                index = ord(item) + (index << 5) + index
        elif type(key) == int:
            index = key + (index<<5) + index

        return index%self._capacity

    def equals(self, key1, key2):
        return key1 == key2

    

# Required Function
def word_frequency(seq):
    hashwd = HashMap()
    for item in seq:
        if item in hashwd:
            hashwd[item] = hashwd[item] + 1
        else:
            hashwd[item] = 1

    return hashwd
