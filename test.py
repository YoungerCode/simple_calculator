
'''def add(*n):
    sum =0
    for num in n:
        sum +=num
    return sum


def multiply(*n):
    sum =1
    for num in n:
        sum *=num
    return sum

print(add(1,2))
print(multiply(2,2))'''


import test_function as t

def test_add():
    assert t.add(0,0)== 0
    assert t.add(-1,-1)== -2
    assert t.add(4,5)== 9
    assert t.add(1,2)== 3
    assert t.add(1,2,3,4)== 10
    assert t.multiply(1,2) == 2
    assert t.multiply(1,2,3,4) == 24

      