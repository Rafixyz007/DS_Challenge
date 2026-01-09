## 4. Micro Challenge: The One-Time Trap

## Goal: Create a generator g loop through it once. Try to loop through it again

g = (i for i in range(100))

print(list(g))
print(list(g))