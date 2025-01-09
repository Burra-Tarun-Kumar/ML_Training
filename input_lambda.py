def add(x,y):
    return lambda x, y: x + y
def sub(x,y):
    return lambda x, y: x - y
def mul(x,y):
    return lambda x, y: x * y
def div(x,y):
    return lambda x, y: x / y
x=int(input())
y=int(input())
print(add(x,y)(x,y))  
print(sub(x,y)(x,y))
print(mul(x,y)(x,y))
print(div(x,y)(x,y))
