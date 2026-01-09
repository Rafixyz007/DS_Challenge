## 2> Micro Challenge: THe Memory Profile

## Gaol: Compare say.getsizeof() of a list Comprehension vs Generator Expression for 1 million numbers.

import sys

l = [x for x in range(1000001)]


print(sys.getsizeof(l))

g = (x for x in range(1000000))

print(sys.getsizeof(g))

