import pytest
def generator1():
    for i in range(1,10):
        print("before")
        yield i
        print('after')

p=generator1()
print(next(p))
print("main")
print(next(p))
