def add(a, b):
    b += 3
    return a + b

def calculate_result(a, b):
    x = add(a, b)


    return x * 3


z = calculate_result(4, 5)
print(z)
