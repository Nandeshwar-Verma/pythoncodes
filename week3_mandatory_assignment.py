#this is first one
def list_oper(list1,list2):
    #def a sq funtion
    sq=(lambda x:x*x)

    #def a cube function
    cube=(lambda x :x*x*x)

    list1_sq=list(map(sq,list1))
    list1_cube=list(map(cube,list1))

    print('list1 sq :',list1_sq)
    print('list1 cube :',list1_cube)

    #checking for the sq and cube is in list2 or not
    #define a check_element function for two lists
    def chk_element(lista,listb):
        set1=set(lista)
        set2=set(listb)
        if set1.intersection(set2)==set1:
            return True
        else:
            return False

    chk_sq=chk_element(list1_sq,list2)
    chk_cub=chk_element(list1_cube,list2)

    if chk_sq and chk_cub:
        print('sq and cub all in list2')
    elif chk_sq:
        print('only sq are present')
    elif chk_cub:
        print('only cub are present')
    else:
        print('nothing all is present')

if __name__=="__main__":
    #list1=list(set(input('enter numbers with comma')))
    #list2=list(set(input('enter second list with comma')))
    list1=[1,2,3]
    list2=[1,4,16,8]
    print(list1,list2)
    list_oper(list1,list2)
