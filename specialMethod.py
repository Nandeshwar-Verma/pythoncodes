"""This is for special or dunder methods
    special or dunder methods are defined which can be used in the instace definition of better use"""

class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return f"{self.title} is written by {self.author}"
    def __len__(self):
        return self.pages

b=Book('eNVy','Nandan',500)
print(b)
print(len(b))
        
