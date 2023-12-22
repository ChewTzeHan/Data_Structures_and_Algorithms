def rearrange_digits(input_list): 
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    # Use quicksort to sort the input list
    
    QuickSort(input_list, 0, len(input_list) - 1)
    
    current_index = len(input_list) - 1
    Sum_1 = ''
    Sum_2 = ''
    
    # Continuously add the largest value in the sorted list to one of the sums
    while current_index != -1:
        
        if current_index % 2 == 1:
            Sum_1 += str(input_list[current_index])
        
        else:
            Sum_2 += str(input_list[current_index])
        
        current_index -= 1
    
    return (int(Sum_1), int(Sum_2))
    pass

def QuickSort(arr, start_index, end_index):
    
    if end_index <= start_index:
        return
    
    
    pivot_index = QuickSort_slightly(arr, start_index, end_index)
    
    QuickSort(arr, start_index, pivot_index - 1)
    QuickSort(arr, pivot_index + 1, end_index)
    
    return arr
    
def QuickSort_slightly(arr, start_index, end_index):
    
    pivot_index = end_index
    pivot_val = arr[pivot_index]    
    left_index = start_index
    
    while pivot_index != left_index:
        item = arr[left_index]
        
        if item <= pivot_val:
            left_index += 1
            continue
        
        arr[left_index] = arr[pivot_index - 1]
        arr[pivot_index - 1] = pivot_val
        arr[pivot_index] = item
        
        pivot_index -= 1
    
    
    return pivot_index

def test_function(test_case):
    for i in test_case[0]:
        if type(i) != int:
            print("Input list must be an array of integers")
            return
    
    for i in test_case[1]:
        if type(i) != int:
            print("Output list must be an array of integers")
            return
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):

        print("Pass, the sum is: {a}".format(a = sum(output)))
    else:
        print("Fail")


#TEST CASE 1

test_function([[1, 2, 3, 4, 5, 6, 7 , 8, 9, 10], [108642, 97531]])
test_function([[30, 12, 20, 23, 22, 12, 20, 23], [30232012, 23222012]])
test_function([[1, 3, 5, 9, 11, 7], [973, 1151]])
test_function([[5, 5, 5, 5, 5, 5, 5], [555, 5555]])

'''
Expected output:
    Pass, the sum is: 206173
    Pass, the sum is: 53454024
    Pass, the sum is: 2124
    Pass, the sum is: 6110
'''

print('----------------')

#TEST CASE 2 - VERY LARGE NUMBERS

test_function([[12345, 11121314, 678910, 1516171819], [1516171819678910, 1112131412345]])
test_function([[30122023, 2212202023, 3012024, 1012024], [22122020233012024, 301220231012024]])
test_function([[1111111111, 2222222222, 3333333333, 5555555555, 9999999999, 1], [999999999933333333331111111111, 555555555522222222221]])

'''
Expected output:
    Pass, the sum is: 1517283951091255
    Pass, the sum is: 22423240464024048
    Pass, the sum is: 1000000000488888888853333333332
'''

print('----------------')

#TEST CASE 3 - NULL / NON-INTEGER VALUES

test_function([[None, None, None, None], [123, 456]])
test_function([[4, 9, 182, 714, 172], [None, 1151]])
test_function([['Ivy', 'Hortensia', 41, 92, 'Goldmary', 'Rosado'], [41, 92]])
test_function([[9, 12, 415, 736, 515, 1893], ['Celine', None]])

'''
Expected output:
    Input list must be an array of integers
    Output list must be an array of integers
    Input list must be an array of integers
    Output list must be an array of integers
'''