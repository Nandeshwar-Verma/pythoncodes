def palindrome(string):
    """ this is documentation for palindrom"""
    x=len(string)
    if x%2==0:
        y=int(x/2)
        #print(y)
        #print(string[0:y],string[-1:-y-1:-1])
        return string[0:y]==string[-1:-y-1:-1]
    else:
        y=int((x+1)/2)
        #print(y)
        #print(string[0:y-1],string[-1:-y:-1])
        return string[0:y-1]==string[-1:-y:-1]


first=palindrome('helleh')
second=palindrome('helloeh')
third=palindrome('nitin')
print(first,second,third)

print("using filter function")
list_str=['hello','helleh','nitin','nandan']
print(list(filter(palindrome,list_str)))

print("map function")
print(list(map(palindrome,list_str)))


#print(help(palindrome))

