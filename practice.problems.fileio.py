#Problem 1
# Create a new file "practice.txt" using python and add the follwoing data to it.

# Hello everyone. We are learning file I/O Using Java I like programming in Java.

with open("practice.txt", "w") as f: 
    data = f.write("Hello Everyone.\nWe are learning file I/O Using Java\nI like programming in Java")


#Problem 2 

#WAF that replace all occurances of "JAVA" with python in the above file.

with open("practice.txt", "r") as f:
    data = f.read()

    updatedWord = data.replace("Java", "Python")

    with open("practice.txt", "w") as f:
        f.write(updatedWord)