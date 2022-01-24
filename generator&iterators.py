""" generators and iterators"""

def gene_cube(n):
        for num in range(n):
                yield num**3

#for x in gene_cube(5):
 #       print(x)

s=gene_cube(5)
print(next(s))
print(next(s))
print(next(s))

s='hello'
#for i in s:
 #       print(i)

s_iter=iter(s)                  #defining iterable
print(next(s_iter))
print(next(s_iter))

