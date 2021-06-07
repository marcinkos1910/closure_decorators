#Algorithm
# 1. Create decorator
#       - prepare function with closure
#       - add annotation


# def convert_to_html(fn):
#     def inner(name):
#         result = fn(f"<b>{name.title()}</b>")
#         return f"<h1>{result}</h1>"
#
#     return inner

def convert_to_html(tag='h1'):
    def wrapper(fn):
        def inner(name):
            result = fn(f"<b>{name}</b>")
            return f"<{tag}>{result}</{tag}>"
        return inner
    return wrapper


def upper(fn):
    def inner(name):
        return fn(name.title())

    return inner

@upper
@convert_to_html(tag="h2")
def hello(name):
    return f"Hello {name}"


print(hello('pawel'))   #Hello pawel -> <h1>Hello <b>Pawel</b></h1>
