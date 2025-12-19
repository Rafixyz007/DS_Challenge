## 1. Micro Challenge: The Scope Fortress

## Goal: Create a golbal variable x = 10. write a function change_x() that sets x = 20 inside it. print x outside the function.
## Observation: It prints 10, not 20.


x = 10

def change_x():
    x = 20

print(x)