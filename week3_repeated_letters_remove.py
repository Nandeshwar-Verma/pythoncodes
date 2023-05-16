'''3. Write the function string_oper which takes a string as
input and return another string after removing the words that have
characters repeated in them
'''
#x='hammer and tom this is sammuel'
def string_oper(string1):
    y=string1.split()
    print(y)
    list1=list()

    def chk_rep(str1):
        check =False
        list1=list()
        for i in str1:
            list1.append(i)
        set1=set(list1)
        if len(set1)==len(list1):
            check=True
            return check
        return check
    ans=''
    for i in y:
        if chk_rep(i):
            ans=ans+ ' '+i
        print(chk_rep(i))
    print(ans.strip())





if __name__=="__main__":
    str1=str(input('give your string'))
    string_oper(str1)