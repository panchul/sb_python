
# "x" - Create - will create a file, returns an error if the file exist
# Write Only (‘w’) : Open the file for writing. For an existing file, the data is truncated and over-written.
#        The handle is positioned at the beginning of the file. Creates the file if the file does not exist.
# Write and Read (‘w+’) : Open the file for reading and writing. For an existing file, data is truncated and
#        over-written. The handle is positioned at the beginning of the file.
# Append Only (‘a’) : Open the file for writing. The file is created if it does not exist. The handle is
#        positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

myfilename = "tmp/demofile1.txt"

f = open(myfilename, "w")
f.write("Now the file has some content!\n")
f.close()

f = open(myfilename, "a")
f.write("Now the file has more content!\n")
f.close()

f = open(myfilename, "r")
aaa = f.read()
f.close()

print(aaa)

# more idiomatic usage

L = ["aaa \n", "bbb \n"]

with open(myfilename, "w") as file1:
    file1.write("Hello \n")
    file1.writelines(L)

with open(myfilename, "r+") as file1:
    print(file1.read()) 

# other functions

file1 = open(myfilename,"w")

# \n is placed to indicate EOL (End of Line) 
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes 

file1 = open(myfilename,"r+")

print("Output of Read function is ")
print(file1.read())

# seek(n) takes the file handle to the nth 
# bite from the beginning. 
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())

file1.seek(0)

# To show difference between read and readline 
print("Output of Read(9) function is ")
print(file1.read(9))

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
# readlines function 
print("Output of Readlines function is ")
print(file1.readlines())
file1.close() 
