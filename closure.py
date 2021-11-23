def sentence(name):
    age = 36
    lol = 30

    def full_sentence(city):
        return f"I am {name}, {age} years-old, from {city}"

    return full_sentence


s = sentence("Pawel")
print(s("Krakow"))


# uuid - universal unique identifier
def gen_uuid():
    idx = 0

    def inner():
        nonlocal idx
        result = idx
        idx += 1
        pass

    return inner

x = 10
uuid = gen_uuid()

# for _ in range(10):
#     print(uuid())

def my_power(exponent):
    lol = 42
    def inner(digit):
        x = lol
        return digit ** exponent
    return inner
power_3 = my_power(3)
power_4 = my_power(4)
power_7 = my_power(7)
print(power_3(2))
print(power_3(3))
print('power_3 what is in closure', power_3.__closure__[0].cell_contents)
print('power_3 what is in closure', power_3.__closure__[1].cell_contents)
print(power_4(2))
print('power_4 what is in closure', power_4.__closure__[0].cell_contents)
print(power_7(2))
print('power_7 what is in closure', power_7.__closure__[0].cell_contents)


def fn(func):
    def wrapper(a):
        def inner(n):
            return func(a) ** n
        return inner
    return wrapper


@fn
def fn_dec(a):
    return a


p = fn_dec(3)
print(p(3))
print(p(4))


