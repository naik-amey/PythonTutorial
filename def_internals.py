
def add(x, y=1):
    return x + y

'''
you can use this to figure out details of a function in python 

add.__code__.co_argcount         add.__code__.co_lnotab
add.__code__.co_cellvars         add.__code__.co_name
add.__code__.co_code             add.__code__.co_names
add.__code__.co_consts           add.__code__.co_nlocals
add.__code__.co_filename         add.__code__.co_posonlyargcount
add.__code__.co_firstlineno      add.__code__.co_stacksize
add.__code__.co_flags            add.__code__.co_varnames
add.__code__.co_freevars         add.__code__.replace(
add.__code__.co_kwonlyargcount 

'''

print(add.__code__.co_argcount)
print(add.__code__.co_code)
print(add.__code__.co_filename)
print(add.__code__.co_name)
print(add.__code__.co_nlocals)
print(add.__code__.co_stacksize)

# inspect has lot of interesting imports. These can be used to get the details about the function. 

from inspect import getsourcefile, getfile, getsource
print(getsource(add))
print(getsourcefile(add))
print(getfile(add))
