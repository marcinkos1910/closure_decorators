queue = []

def add_to_queue(item):
    queue.append(item)



def remove_from_queue():
    queue.pop(0)


# print(queue)
# add_to_queue("a")
# print(queue)
# add_to_queue("b")
# print(queue)
# remove_from_queue()
# print(queue)



stack = []


def add_to_stack(item):
    stack.append(item)


def remove_from_stack():
    stack.pop()


print(stack)
add_to_queue("a")
print()
