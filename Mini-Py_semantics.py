# Name:
# Student ID:
# Look at each Mini-Py code and decide whether it will pass the semantics check or not. Explain the type/cause of the error (if applicable).

# part a
def foo(a:int, b:int)->int:
    print(a, b)
    if b <= 0:
        a:int = -1

    return a + b
    
    
# part b
if False + 1:
    print("True")

# part c
def foo(a:int, b:int)->int:
    print(a, b)
    a:int
    if b <= 0:
        a = -1 

    return a + b

    
#part d
def print_list(arr:[[int]]):

    i:int              
    for i in arr:
        print(i)
        

# part e
k:int
def odd_even(a:int):

    k = a % 2 == 0
    return k
    
#part f
def foobar(i:int, b:bool, s:str, li:[[int]]):
    if b:
        print(s)
    if i in li:
        print(True)

foobar(2, "False", True, 5)
