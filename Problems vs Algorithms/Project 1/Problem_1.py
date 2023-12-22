def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    
    if type(number) != int or number < 0:
        return None
    
    return int((number**0.5) // 1)


#TEST CASE 1

print ("Number: {a} Result: {b} ".format(a = sqrt(64), b = "Pass" if (8 == sqrt(64)) else "Fail"))
print ("Number: {a} Result: {b} ".format(a = sqrt(81), b = "Pass" if (9 == sqrt(81)) else "Fail"))
print ("Number: {a} Result: {b} ".format(a = sqrt(100), b = "Pass" if (10 == sqrt(100)) else "Fail"))
print ("Number: {a} Result: {b} ".format(a = sqrt(144), b = "Pass" if (12 == sqrt(144)) else "Fail"))

'''
Expected output: 
    Number: 8 Result: Pass 
    Number: 9 Result: Pass 
    Number: 10 Result: Pass 
    Number: 12 Result: Pass 
'''

print('----------------')

#TEST CASE 2 - NONE / NON-INTEGER VALUES

print ("Number: {a} Result: {b} ".format(a = sqrt(None), b = "Pass" if (None == sqrt(None)) else "Fail"))
print ("Number: {a} Result: {b} ".format(a = sqrt('Merry Christmas'), b = "Pass" if (None == sqrt('Merry Christmas')) else "Fail"))

'''
Expected output:
    Number: None Result: Pass 
    Number: None Result: Pass
'''
print('----------------')

#TEST CASE 3 - VERY LARGE NUMBERS

print ("Number: {a} Result: {b} ".format(a = sqrt(30122023), b = "Pass" if (5488 == sqrt(30122023)) else "Fail"))
print ("Number: {a} Result: {b} ".format(a = sqrt(12345678910), b = "Pass" if (111111 == sqrt(12345678910)) else "Fail"))
print ("Number: {a} Result: {b} ".format(a = sqrt(20230301), b = "Pass" if (4497 == sqrt(20230301)) else "Fail"))

'''
Expected output:
    Number: 5488 Result: Pass 
    Number: 111111 Result: Pass 
    Number: 4497 Result: Pass 
'''

