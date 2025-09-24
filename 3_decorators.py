def simple_deco():
    def deco(ori_fun):
        def inner():
            print("before running original function")
            ori_fun()
            print("After running original function")

        return inner

    @deco
    def Hello():
        print("Hello")

    Hello()


def ntimes():
    def repeat(n):
        def deco(ori_func):
            def inner_func(*args, **kargs):
                for _ in range(n):
                    ori_func(*args, *kargs)

            return inner_func

        return deco

    @repeat(2)
    def add(a, b):
        print(a + b)

    add(2, 3)


def twice():
    def log(msg):
        print(msg)

    def deco_twice(ori_func):
        def inner_function(*args):
            ori_func(*args)
            ori_func(*args)

        return inner_function

    @deco_twice
    def fun1(*arg):
        print(f"original function:{arg}")

    fun1("ram")


def timetaken():
    from datetime import datetime

    def it_time(ori_func):
        def inner_func(*args, **kargs):
            before = datetime.now()
            result = ori_func(*args, **kargs)  # store the return value
            after = datetime.now()
            exectime = after - before
            print("Execution time:", exectime)
            return result  # return it so the caller gets the actual output

        return inner_func

    @it_time
    def add(a, b):
        return a + b

    print("Sum is:", add(5, 7))


def upper():
    @to_upper
    def greet(name):
        return f"Hello {name}"

    print(greet("ram"))


if __name__ == "__main__":
    # Write a decorator that prints "Before" before the wrapped function runs and "After" after it runs.
    # simple_deco()

    # run function n times
    ntimes()
    # Create a decorator that runs the wrapped function twice whenever it is called.
    twice()

    # Create a decorator @time_it that measures how long a function takes to run.
    timetaken()

    # Write a decorator that converts the return value of the wrapped function to uppercase.
    upper()
