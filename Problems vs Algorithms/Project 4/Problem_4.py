def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
    next_0_index = 0
    next_2_index = len(input_list) - 1
    
    current_index = 0
    
    while current_index <= next_2_index:
        
        if input_list[current_index] == 0:
            input_list[current_index] = input_list[next_0_index]
            input_list[next_0_index] = 0
            current_index += 1
            next_0_index += 1
        
        elif input_list[current_index] == 2:
            input_list[current_index] = input_list[next_2_index]
            input_list[next_2_index] = 2
            next_2_index -= 1
        
        else:
            current_index += 1
            
    
    return input_list


def test_function(test_case):
    for i in test_case:
        if i != 0 and i != 1 and i != 2:
            print("Input array must only contain 0, 1 & 2")
            return
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass, sorted array is: {a}".format(a = sorted_array))
    else:
        print("Fail")


#TEST CASE 1

test_function([0,2,1,2,2,2,2,0,0,0,0,1,1,2])
test_function([1,1,1,1,1,1,1,1,0,0,0,2,2,2,2,2,2,2,2,0,0,0,1])
test_function([2,1,2,1,1,0,1,0,0,0,2,2,1,0])

'''
Expected output:
    Pass, sorted array is: [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    Pass, sorted array is: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
    Pass, sorted array is: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2]
'''

print('----------------')
#TEST CASE 2 - NONE / NON- 0,1,2 INTEGER VALUES

test_function([None, None, 1,0,0,0,1,2,2,2,1])
test_function(['Terakomari', 2,1,2, 'Sakuna', 'Vill', 1, 2 ,2 ,0])
test_function([3,4,5,6,7,8,9,1,2,0,0,0,0,1,1,1,2,2,2])

'''
Expected output:
    Input array must only contain 0, 1 & 2
    Input array must only contain 0, 1 & 2
    Input array must only contain 0, 1 & 2
'''
print('----------------')
#TEST CASE 3 - VERY LARGE ARRAYS
import random
random.seed(69)

array, array1 = [], []
for i in range(0, 100):
    array.append(random.randint(0, 2))
    
for i in range(0, 200):
    array1.append(random.randint(0, 1))

test_function([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1])
test_function(array)
test_function(array1)


'''
Expected output:
    Pass, sorted array is: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    Pass, sorted array is: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    Pass, sorted array is: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
'''