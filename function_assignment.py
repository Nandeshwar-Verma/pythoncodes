"""this is for function retruning function and function assignment"""

def hello():
        #print("Hello nands")
        def hi():
                return "hi Nands"
        return hi()

hello()
print(hello)
""" function assignment"""
another_hello=hello
print(another_hello)
print(another_hello())



""" function as an argument"""
def hello(name):
        #return name
        print(name())                   #executing the funtion as argument

def display():
        print("my name is Nands")

hello(display)                          #passing function as agument
