## 3. Micro Challenge: The Default Gateway

## Goal: Write a function connect(port=3306) that prints "Connecting to [port]". call it once with no arguments, and once with 5432.

def connect(port=3306):
    print("Connecting to", port)

connect()
connect(5432)