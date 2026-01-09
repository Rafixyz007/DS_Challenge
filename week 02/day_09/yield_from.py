## 8. Micro Challenge: Yield From

## Goal: Write a generator that yields a values from two different sub-generators using yield from.

num = range(101)

def squares(nums):
    for i in nums:
        yield i * i

def filter_even(nums):
    for i in nums:
        if i % 2 == 0:
            yield i

def combine_fun():
    yield from filter_even(squares(num))

for value in combine_fun():
    print(value)




    """
    Combine multiple sub-generators into a single pipeline using `yield from`.

    This generator first yields squared values produced by the `squares` generator
    and then filters those values to yield only the even results. The delegation
    is handled using `yield from` for clean and memory-efficient chaining.
    """