## 10. Micro Challenge: State Retention

## Goal: Write a generator that calculates a "Running Average"

def average():
    total = 0
    count = 0
    num = yield
    while True:
        total = total + num
        count = count + 1
        num = yield total/count

gen = average()

next(gen)

print(gen.send(10))
print(gen.send(20))
print(gen.send(40))
print(gen.send(34))
print(gen.send(23))


"""
    A generator that calculates the running average of numbers sent to it.

    The generator maintains a running total and count of all numbers received.
    Each time a number is sent using `send()`, it updates the total and count,
    then yields the current average. The generator runs indefinitely, allowing
    continuous streaming of numbers.

    Usage:
        gen = running_average()
        next(gen)             # prime the generator
        gen.send(10)          # returns 10.0
        gen.send(20)          # returns 15.0
        gen.send(30)          # returns 20.0

    Yields:
        float: The current running average of all numbers received so far.
"""