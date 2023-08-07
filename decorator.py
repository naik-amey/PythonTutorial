from time import time 

'''
Suppose I want to time the add function. and sub function. 
To calculate the time, I need to always do the following. 
time_start = time()
add(1,2)
print(f'time taken, {time() - time_start}')
time_start = time()
add(2,5)
print(f'time taken, {time() - time_start}')
time_start = time()
sub(10,5)
print(f'time taken, {time() - time_start}')

Is there a better way?
'''

# YES. create a wrapper function. 

def timer(func):
    def f(x,y):
        time_start = time()
        rv = func(x,y)
        print(f'time taken : {time() - time_start}')
        return rv
    return f

def add(x, y=1):
    return x + y
add = timer(add)

def sub(x, y=1):
    return x + y
sub = timer(sub)

print(add(2234134134,3000000))

# INSTEAD of add = timer(add) ; you can use a decorator. 

@timer
def add(x, y=1):
    return x + y

print(add(2234134134,3000000))


# MORE generally we can define decorator class as follows

def timer(func):
    def f(*args,**kwargs):
        time_start = time()
        rv = func(*args,**kwargs)
        print(f'time taken : {time() - time_start}')
        return rv
    return f

@timer
def add(x, y=1):
    return x + y


@timer
def mul(x, y, z):
    return x * y * z

print(add(2234134134,3000000))
print(mul(12,123,1234))