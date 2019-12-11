def add(*n):
    sum =0
    for num in n:
        sum +=num
    return sum


def multiply(*n):
    product =1
    for num in n:
        product *=num
    return product

print(add(1,2))
print(multiply(2,2))
