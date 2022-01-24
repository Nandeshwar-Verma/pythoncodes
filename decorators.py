""" decorators"""
def decorator_func(original_func):
        def wrap_func():
                print("something before wrapping")
                original_func()
                print("something after wrapping")
        return  wrap_func

@decorator_func                         #comment out @ operator and below function will execute alone
def need_decoration():
        print("i need decoration")

need_decoration()               #this is work as decorated function until the above @ is commented


""" The above is similar to below


func_need_decoration=decorator_func(need_decoration)     #this is for function assignment
func_need_decoration()
"""
                

