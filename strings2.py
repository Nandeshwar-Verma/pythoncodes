#this is for string part 2 

#escape characer- helps in inserting many functions in the string

A="This is example one of \"ESCAPE\" character in strings"
print(A)

#next line

B="This is for \n next line \n formulation in strings and \n back slash \\ example combined"
print(B)

C="i am NV. my place is Mfp."
print(C.capitalize())

#casefold - Converts string into lower case

"""C="This is Test"
X=C.casefold()
print(X)       #Converts string into lower case"""

#center()
X="banana"
print(X.center(20))
print(X.center(20,"@"))

""" Sample test in between"""
Y=C[2:3]
print("value of Y",Y)
Z=Y in X
W=Y not in X
if 4 <3 :
 print(Z)
print(W)

#count() - count number of occurences

txt=" This is just a random check for this being printed this many times"
print("This is in txt for",txt.count("this"))
print("this is in txt from 1-20",txt.count("this",30,40))