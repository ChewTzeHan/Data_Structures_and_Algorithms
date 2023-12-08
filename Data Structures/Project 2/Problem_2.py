import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    lists = list()
    
    check_suffix(suffix, lists, path)
        
    return lists

def check_suffix(suffix, lists, path):
    
    for i in os.listdir(path):
        if i.endswith(suffix):
            lists.append(os.path.join(path, i))
        elif os.path.isdir(os.path.join(path, i)):

            check_suffix(suffix, lists, os.path.join(path, i))
        
        


found_files = find_files('.c', "./testdir" )


print('.c files found:')
for i in found_files:
    print(i)

print('---------------')
## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

test_files_1 = find_files('.c', "./Test_Folder_1" )

print('.c files found:')
for i in test_files_1:
    print(i)

'''
Expected output: 
    ./Test_Folder_1\Friday\Saturday\Outing.c
    ./Test_Folder_1\Friday\Saturday\Stay at home.c
    ./Test_Folder_1\Friday\Sunday\Laze about.c
    ./Test_Folder_1\Monday.c
    ./Test_Folder_1\Thursday\Wednesday\Tuesday\Walk.c
    ./Test_Folder_1\Tuesday\Eat.c
    ./Test_Folder_1\Wednesday\Wednesday\Sleep.c
'''
print('---------------')

## Test Case 2 EDGE CASE: Odd file name values & Capitalized file extensions

test_files_2 = find_files('.py', "./Test_Folder_2" )

print('.py files found:')
for i in test_files_2:
    print(i)


'''
Expected output:
    .py files found:
    ./Test_Folder_2\Brodia\Alcryst.py.py.py.py
    ./Test_Folder_2\Brodia\Diamant.py
    ./Test_Folder_2\Elusia\Hortensia.PY.py
    ./Test_Folder_2\Elusia\Ivy.py
    ./Test_Folder_2\Firene\Alfred.py
    ./Test_Folder_2\Firene\Celine.py.py
    ./Test_Folder_2\Solm\Fogado.PY.Py.pY.py
    ./Test_Folder_2\Solm\Timerra.py
    ./Test_Folder_2\Sommie.py
'''
print('---------------')

## Test Case 3 EDGE CASE: Large subdirectories & empty files

test_files_2 = find_files('.exe', "./Test_Folder_3" )

print('.exe files found:')
for i in test_files_2:
    print(i)
    
#Expected output:  
    #.exe files found:
    #./Test_Folder_3\Large Subdirectories.exe
    #./Test_Folder_3\Sakuna\.exe
    #./Test_Folder_3\Sakuna\Memoir\Sakuna Memoir.exe
    #./Test_Folder_3\T\E\R\A\K\O\M\A\R\I\Terakomari.exe
    #./Test_Folder_3\T\E\R\A\K\O\M\A\R\I\_\G\A\N\D\E\S\B\L\O\O\D\Terakomari_Gandesblood.exe
    #./Test_Folder_3\Villhaze\.            .exe
    #./Test_Folder_3\Villhaze\..exe





