## 9. Maicro Challenge: The Send Method

## Goal: Use gen.send(value) to inject data into running generator.


def square():
    num = yield
    while True:
        num = yield num * num

gen = square()

next(gen)
print(gen.send(10))
# print(next(gen))
print(gen.send(2))
# print(next(gen))
print(gen.send(13))


"""
    A generator that calculates the square of numbers sent to it.

    This generator waits for a number to be sent using the `send()` method,
    then yields the square of that number. It maintains an infinite loop,
    so it can continuously process numbers one by one without restarting.

    Usage:
        gen = square()
        next(gen)             # prime the generator
        gen.send(10)          # returns 100
        gen.send(2)           # returns 4
        gen.send(13)          # returns 169

    Yields:
        int: The square of the number sent into the generator.
    """
