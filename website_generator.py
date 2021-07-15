def make_website(placeholder, input_file="index.html"):
    def wrapper(fn):
        def inner(*args):
            result = fn(*args)

            with open(input_file, "r") as file:
                new_lines = []
                for line in file.readlines():
                    if "{{" + placeholder + "}}" in line:
                        new_lines.append(line.replace("{{" + placeholder + "}}", result))
                    else:
                        new_lines.append(line)

            with open(f"{args[-1]}.html", "w") as file:
                file.writelines(new_lines)

            return result

        return inner

    return wrapper


def convert_to_html(tag='h1', color="peru"):
    def wrapper(fn):
        def inner(*args):
            tag_parameters = [f'<b style="color: {color};">{arg}</b>' for arg in args]
            result = fn(*tag_parameters)
            return f"<{tag}>{result}</{tag}>"

        return inner

    return wrapper


def upper(fn):
    def inner(*args):
        upper_name = [arg.title() for arg in args]
        return fn(*upper_name)

    return inner


@make_website("placeholder", input_file="welcome.html")
@upper
@convert_to_html(color="gold")
def hello(name):
    return f"Hello {name}"


@make_website("placeholder", input_file="welcome.html")
@upper
@convert_to_html(color="gold")
def goodbye(firstname, lastname):
    return f"Goodbye {firstname} {lastname}"


print(hello('jessica'))  # generate website
print(goodbye('jessica', 'biel'))
