## 3.Micro Challenge: THe Infinite Sequence

## Goal: Write a while True generator that produces Fibonacci numbers forever.

def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b


fib = fibonacci()

for _ in range(10):
    print(next(fib))



    
