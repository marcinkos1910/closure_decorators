def upper_decorator(fn):
    def inner(name):
        return fn(name.title())

    return inner

def upper(fn, value):
    return fn(value.title())

@upper_decorator
def hello(name):
    return f"Hello {name}"


@upper_decorator
def goodbye(name):
    return f"Goodbye {name}"


# print(hello("pawel"))
# print(goodbye("pawel"))

# u = upper_decorator(hello)
# print(u('pawel'))
#
# g = upper_decorator(goodbye)
# print(g('pawel'))

# print(upper_decorator(hello)('pawel'))

print(hello("pawel"))