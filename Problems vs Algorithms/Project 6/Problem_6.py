import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    
    high, low = ints[0], ints[0]
    
    for i in ints:
        if type(i) == int:
            if type(high) != int:
                high, low = i, i
            if i > high:
                high = i
            
            elif i < low:
                low = i
    
    return (low, high)


#TEST CASE 1

test_list_1 = [i for i in range(0, 20)]
test_list_2 = [i for i in range(10, 20)]
test_list_3 = [i for i in range(30, 50)]

random.shuffle(test_list_1)
random.shuffle(test_list_2)
random.shuffle(test_list_3)

print("Lowest and Highest numbers are: {a}".format(a = get_min_max(test_list_1)))
print("Lowest and Highest numbers are: {a}".format(a = get_min_max(test_list_2)))
print("Lowest and Highest numbers are: {a}".format(a = get_min_max(test_list_3)))


'''
Expected output:
    Lowest and Highest numbers are: (0, 19)
    Lowest and Highest numbers are: (10, 19)
    Lowest and Highest numbers are: (30, 49)
'''
print('----------------')
#TEST CASE 2 - VERY LARGE NUMBERS

test_list_4 = [i for i in range(0, 21366)]
test_list_5 = [i for i in range(0, 768569, 2)]
test_list_6 = [i for i in range(999, 12894, 3)]

random.shuffle(test_list_4)
random.shuffle(test_list_5)
random.shuffle(test_list_6)

print("Lowest and Highest numbers are: {a}".format(a = get_min_max(test_list_4)))
print("Lowest and Highest numbers are: {a}".format(a = get_min_max(test_list_5)))
print("Lowest and Highest numbers are: {a}".format(a = get_min_max(test_list_6)))

'''
Expected output:
    Lowest and Highest numbers are: (0, 21365)
    Lowest and Highest numbers are: (0, 768568)
    Lowest and Highest numbers are: (999, 12891)
'''

print('----------------')
#TEST CASE 3 - NULL / NON-INTEGER VALUES

test_list_7 = [None, None, 3,2,1,5,4, None]
test_list_8 = ['Terakomari', 12, 13, 62, 'Villhaze', 59, 83, 74, 'Sakuna']

print("Lowest and Highest numbers are: {a}".format(a = get_min_max(test_list_7)))
print("Lowest and Highest numbers are: {a}".format(a = get_min_max(test_list_8)))

'''
Expected output:
    Lowest and Highest numbers are: (1, 5)
    Lowest and Highest numbers are: (12, 83)
'''