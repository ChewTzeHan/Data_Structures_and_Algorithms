class LRU_Cache(object):

    def __init__(self, capacity = 5):
        # Initialize class variables
        
        self.cache_size = capacity
        self.current_size = 0
        self.elements = {}
        self.priority = []
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        
        if key in self.elements:
            self.priority.remove(key)
            self.priority.insert(len(self.priority), key)
            
            return self.elements[key]
        
        else:
            return -1
        
        
        
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.        
        
        if type(key) != int or type(value) != int:
            return
        
        if key in self.elements:
            return
        
        if self.current_size >= self.cache_size:
            rmv = self.priority.pop(0)
            del self.elements[rmv]
            self.current_size -= 1
                    
        self.elements[key] = value
        self.priority.append(key)
        self.current_size += 1  
        
           
        
        pass

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache



our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry



## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values
print('--------------------')
## Test Case 1

test_cache_1 = LRU_Cache()

test_cache_1.set(5, 11)
test_cache_1.set(7, 9)
test_cache_1.set(10, 25)
test_cache_1.set(9, 2)

print(test_cache_1.get(7)) # returns 9
print(test_cache_1.get(9)) # returns 2
print(test_cache_1.get(3)) # returns -1 as 3 is not present in the cache

test_cache_1.set(6, 9)
test_cache_1.set(10, 12)

print(test_cache_1.get(10)) # returns 25 as key was already present before
print(test_cache_1.get(5)) # returns 11 as set(10, 12) did not go through, thus least used cache was not removed




print('--------------------')
## Test Case 2, EDGE CASE: Non-digit & empty values


test_cache_2 = LRU_Cache()

test_cache_2.set('Yes', 'No')
test_cache_2.set(1,2)
test_cache_2.set(2,4)
test_cache_2.set(3,6)
test_cache_2.set(4,8)
test_cache_2.set('Claire', 'Rae')



print(test_cache_2.get('Yes')) # returns -1 as 'Yes' was not set as key only accepts integers
print(test_cache_2.get(3)) # returns 6
print(test_cache_2.get('Claire')) # returns -1 as 'Claire' was not set as key only accepts integers


test_cache_2.set(5,None)
test_cache_2.set(6, 12)

print(test_cache_2.get(5)) # returns -1 as '5' was not set as value given was not integer
print((test_cache_2.get(6))) # returns 12


print('--------------------')
## Test Case 3, EDGE CASE: Very large values

test_cache_3 = LRU_Cache()

test_cache_3.set(123456, 789012)
test_cache_3.set(13579, 246810)
test_cache_3.set(987654321, 3)
test_cache_3.set(3, 12345678910)
test_cache_3.set(9122023, 30122023)


print(test_cache_3.get(123456)) # returns 789012
print(test_cache_3.get(987654321)) # returns 3
print(test_cache_3.get(3)) # returns 12345678910
print(test_cache_3.get(2122023)) # returns -1 as key 2122023 does not exist



print('--------------------')
