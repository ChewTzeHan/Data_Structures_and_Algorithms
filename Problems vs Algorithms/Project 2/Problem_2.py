def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    high = len(input_list) - 1
    low = 0
    
    # Find where the array is pivoted at
    pivot = PivotedNum(input_list, low, high)
    
    
    if input_list[pivot] == number:
        return pivot
    
    #Split array into 2 that are both sorted, find number's index in either array
    
    if input_list[0] <= number:
        return binary_search(input_list, 0, pivot - 1, number)
    
    return binary_search(input_list, pivot + 1, high, number)

def PivotedNum(arr, low, high):
    
    if high < low:
        return -1
    if high == low:
        return low
    
    mid = (high + low) // 2
    
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return PivotedNum(arr, low, mid - 1)
    return PivotedNum(arr, mid + 1, high)
    

def binary_search(arr, low, high, number):
    
    mid = (high + low) // 2
    
    
    
    if arr[mid] == number:
        return mid
    
    if high < low:
        return -1
    
    
    elif number > arr[mid]:
        return binary_search(arr, mid + 1, high, number)
    
    return binary_search(arr, low, mid - 1, number)
        
    

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    for i in test_case[0]:
        if type(i) != int:
            print("Input list must be an array of sorted integers")
            return
        
    if type(test_case[1]) != int:
        print('Input number must be an integer')
        return
    
    input_list = test_case[0]
    number = test_case[1]
    linear_result = linear_search(input_list, number)
    if linear_result == rotated_array_search(input_list, number):
        if linear_result == -1:
            linear_result = 'not found'
        print("Pass, the index of {a} is {b}".format(a = number, b = linear_result))
    else:
        print("Fail")


#TEST CASE 1

test_function([[12, 13, 14, 15, 9, 10, 11], 10])
test_function([[23, 24, 17, 18, 19, 20, 21, 22], 21])
test_function([[33, 34, 35, 36, 37, 38, 32], 37])

'''
Expected output:
    Pass, the index of 10 is 5
    Pass, the index of 21 is 6
    Pass, the index of 37 is 4
'''
print('----------------')

#TEST CASE 2 - VERY LARGE NUMBERS

test_list = []
for i in range(32, 99):
    test_list.append(i)
for i in range(2, 32):
    test_list.append(i)
test_function([[20231221, 20231222, 20231223, 20231218, 20231219, 20231220], 20231219])
test_function([test_list, 87])
test_function([[111111111, 111111112, 111111113, 111111108, 111111109, 1111111110], 1111111111])


'''
Expected output:
    Pass, the index of 20231219 is 4
    Pass, the index of 87 is 55
    Pass, the index of 1111111111 is not found
'''
print('----------------')

#TEST CASE 3 - NONE / NON-INTEGER VALUES

test_function([[None, None, None, None], 32])
test_function([[33, 34, 35, 36, 37, 38, 32], None])
test_function([['Sakuna', 'Vill', 12, 13, 'Karla', 'Nelia'], 15])
test_function([[21, 22, 23, 24, 18, 19, 20], 'Terakomari'])

'''
Expected output:
    Input list must be an array of sorted integers
    Input number must be an integer
    Input list must be an array of sorted integers
    Input number must be an integer
'''