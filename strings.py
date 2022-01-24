A='''this is for strings theory 
     a string is just array of character as there is no single character concept in python
     a single character can be understood as string of length 1'''

print(A)
print("print only first character of above string")
print(A[0])
print("remember that the first character has the position 0")

#SLICING- This takes a piece of string starting to end of position 
print(A[1:7])
#negative indexing- this will read from end of string
print("negative indexing- this will read from end of string") 
print("")
print("reading from back of string possition 8 to 2",A[-8:-2])

#get length of string String Length
print("length of string is : ",len(A))

#strip method to remove any blank space at beginning and end of the string

B="""   This is example of strip method as WELL as upper case and LOWER case  """
print("before strip:",B)
print("after strip:",B.strip())

#lower case
print(B.lower())

#upper case

print(B.upper())

#replace 

print(B.replace("case","Cause"))

#split method - to spilt string into substring
print(B.split("as"))

#find string

X="upper" in B
print(X)

#not in string
Y="upper" not in B
print(Y)

#format function to insert numbers in text 
age=34
salary=1000
height=5.6
details="my name is Nandeshwar. My age is {}"
print(details.format(age))
details1="my name is nandeshwar.my age is {} and salary is {} and height is {}"
print(details1.format(age,salary,height))

details3="my name is NV. My age is {2} and salary is {0} and height is {1}"
print(details3.format(salary,height,age))

C=B.lower()
print(C)

D=A[0:5]
print(D)

E=B.replace("as","AS")
print(E)

