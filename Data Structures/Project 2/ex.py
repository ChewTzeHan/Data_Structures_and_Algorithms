### Locally save and call this file ex.py ##

## Code to demonstrate the use of some of the OS modules in python

import os

## Let us print the files in the directory in which you are running this script
print (os.listdir("./testdir"))
print(type(os.listdir("./testdir")))

print(os.path.isdir('./testdir'))

print('----')

path = './testdir'
for i in os.listdir(path):
    print(os.path.join(path, i))
    #if i.endswith('.c'):
    #    print(i)

print('----------')

## Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

## Does the file end with .py?
print ("./ex.py".endswith(".py"))


print(os.listdir('./testdir'))

path = "/home"
 
# Join various path components 
print(os.path.join(path, "User/Desktop", "file.txt"))