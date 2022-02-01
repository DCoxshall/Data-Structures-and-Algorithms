def make_pretty(func):
    def new_func(*args, **kwargs):
        print("########")
        print(func(*args, **kwargs))
        print("########")

    return new_func


@make_pretty
def add(a, b):
    return a + b


print(add(5, 4))
