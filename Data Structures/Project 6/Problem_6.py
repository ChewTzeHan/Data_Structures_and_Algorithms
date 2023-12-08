from datetime import datetime

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        
        if value is None:
            return
        
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    
    cur_element = llist_1.head
    
    union_list = []
    union_llist = LinkedList()
    
    
    while cur_element:
        if cur_element.value not in union_list:        
            union_list.append(cur_element.value)
        cur_element = cur_element.next
    
    #print(union_list)
    
    cur_element = llist_2.head
    
    while cur_element:
        if cur_element.value not in union_list:        
            union_list.append(cur_element.value)
        cur_element = cur_element.next
        
        
    #print(union_list)
    
    
    for i in union_list:
        union_llist.append(i)
        
    return union_llist

def intersection(llist_1, llist_2):
    # Your Solution Here
    
    cur_element_1 = llist_1.head
    
    intersection_list = []
    intersection_llist = LinkedList()
    
    while cur_element_1:
        if cur_element_1.value not in intersection_list:
            
            cur_element_2 = llist_2.head
            
            while cur_element_2:
                if cur_element_1.value == cur_element_2.value:
                    intersection_list.append(cur_element_1.value)
                    break
                
                cur_element_2 = cur_element_2.next       
                    
        cur_element_1 = cur_element_1.next
    
    if len(intersection_list) == 0:
        return 'There are no intersecting values'
    
    else:
        for i in intersection_list:
            intersection_llist.append(i)
    
    return intersection_llist


## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ('Union list: {a}'.format(a = union(linked_list_1,linked_list_2)))
print ('Intersection list: {a}'.format(a = intersection(linked_list_1,linked_list_2)))

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ('Union list: {a}'.format(a = union(linked_list_3,linked_list_4)))
print ('Intersection list: {a}'.format(a = intersection(linked_list_3,linked_list_4)))

print('----------------')


## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1 EDGE CASE: Null/None values

test_list_1 = LinkedList()
test_list_2 = LinkedList()

test_element_1 = [2023, 10, 25, None, 21, 50, 39]
test_element_2 = [None, 2022, 5, 11, 21, 30, 50, None]

for i in test_element_1:
    test_list_1.append(i)

for i in test_element_2:
    test_list_2.append(i)

print ('Union list: {a}'.format(a = union(test_list_1,test_list_2)))
print ('Intersection list: {a}'.format(a = intersection(test_list_1,test_list_2)))


'''
Expected output:
    Union list: 2023 -> 10 -> 25 -> 21 -> 50 -> 39 -> 2022 -> 5 -> 11 -> 30 -> 
    Intersection list: 21 -> 50 -> 
'''
print('----------------')
## Test Case 2 EDGE CASE: Very large values

test_list_3 = LinkedList()
test_list_4 = LinkedList()

test_element_3 = [123456, 78910, 987654321, 5553111, 999666333, 222111222]
test_element_4 = [12345678910, 987654321, 57623016, 67964293, 99966633, 5407184102, 5553111]

for i in test_element_3:
    test_list_3.append(i)

for i in test_element_4:
    test_list_4.append(i)

print ('Union list: {a}'.format(a = union(test_list_3,test_list_4)))
print ('Intersection list: {a}'.format(a = intersection(test_list_3,test_list_4)))

'''
Expected output:
    Union list: 123456 -> 78910 -> 987654321 -> 5553111 -> 999666333 -> 222111222 -> 12345678910 -> 57623016 -> 67964293 -> 99966633 -> 5407184102 -> 
    Intersection list: 987654321 -> 5553111 -> 
'''

print('----------------')
## Test Case 3 EDGE CASE: Different element types

test_list_5 = LinkedList()
test_list_6 = LinkedList()

node = Node(5)

test_element_5 = [node, 'Terakomari', [2023, 2022] , datetime(2023, 12, 9, 9, 30), 123.0]
test_element_6 = [node, "Terakomari", {2023: '2022', 'Yes': 'No'}, datetime(2023, 12, 9, 9, 30), 987.0]

for i in test_element_5:
    test_list_5.append(i)

for i in test_element_6:
    test_list_6.append(i)

print ('Union list: {a}'.format(a = union(test_list_5,test_list_6)))
print ('Intersection list: {a}'.format(a = intersection(test_list_5,test_list_6)))

'''
Expected output:
    Union list: 5 -> Terakomari -> [2023, 2022] -> 2023-12-09 09:30:00 -> 123.0 -> {2023: '2022', 'Yes': 'No'} -> 987.0 -> 
    Intersection list: 5 -> Terakomari -> 2023-12-09 09:30:00 -> 
'''