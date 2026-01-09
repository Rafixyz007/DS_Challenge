## 6. Micro Challenge: The Pipeline (Chaining)

## Goal: Create two generators: one squares numbers, the other filter evens. Chain them: filter(square(num)).

def squares(num):
    for i in num:
        yield i * i



def filter_even(num):
    for i in num:
        if i % 2 == 0:
            yield i


num = range(1,101)

pipeline = filter_even(squares(num))

for i in pipeline:
    print(i)

"""
Created two generators: one that squares numbers and another that filters even values.
The pipeline takes input from the `num` source, computes the square of each value,
and yields only those squared results that are even.
"""
