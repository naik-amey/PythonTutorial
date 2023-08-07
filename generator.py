
# 1st way to write:
class compute:
    def __init__(self):
        self.last = 0

    def __iter__(self):
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        return rv


arr1 = compute()

for ele in arr1:
    print(ele)

# 2nd way to write:

def compute():
    for i in range(10):
        yield i

arr2 = compute()

for ele in arr2:
    print(ele)

# important thing to note here is, we interleave between user call and function call due to yield method. 
# This is a characteristic of generator. 
# generators are mechanism by which you can create code which can interleave with other code and also enforce sequencing.

# this mechanism can be used in a api call. 
'''
for example suppose you develop an api where there are 3 function calls 
'''

def first():
    print("first called")

def second():
    print("second called")

def third():
    print("third called")

class api():
    def call_this_first():
        first()
    def call_this_second():
        second()
    def call_this_third():
        third()

# Assume that api wants to enforce this rule, make sure the order is maintained. 

# this can be enforced using generators.

def api():
    first()
    yield
    second()
    yield
    third()

for _ in api():
    print("I did something")