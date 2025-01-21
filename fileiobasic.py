# Python can be used to perform operations on a file. (Read and Write data)
#TO READ THE ENTIRE FILE
f = open("sample.txt", "r")
data = f.read()
print(data)

#To read the file line 

f = open("sample.txt", "r")

data = f.readline()

print(data.strip()) #strip removes the whitespace

#To write a file

f = open("sample.txt", "w")
f.write("Hello I am no one!")
f.close()

#To Create a file

f = open("sample2.txt", "x")
f.write("Hello I am no one!")
f.close()

#To append to a file

f = open("sample2.txt", "a")
f.write("\t Hello I am going outside tonight!")
f.close()

#with syntax

with open ("sample2.txt", "r") as f:
    data = f.read()
    print(data)


#HOW TO delete files


import os
os.remove("sample2.txt")