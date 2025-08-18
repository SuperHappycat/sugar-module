# Mini Python Shorthand Library – `my_sugar.py`

**Author:** Natee  
**Version:** 0.1  

A lightweight Python library designed to make everyday coding shorter, cleaner, and more readable. It provides shorthand functions for printing, math, strings, flow control, and more.

---

## Features

### 1. Print Multiple Times

printn("Hello", n=3)  # Prints "Hello" 3 times
### 2. Math Utilities
add(1,2,3) # 6

mul(2,3,4) # 24

sq(5)             # 25

cube(3)           # 27

maxit(1,4,2)      # 4

minit(1,4,2)      # 1

reduceit([1,2,3], lambda x,y: x+y)  # 6

### 3. String Utilities

repeat("ha", 3)  # "hahaha"

### 4. Boolean Utilities

yes()  # True
no()   # False

### 5. Function Utilities

@short
def greet():
    print("Hello")

flip(lambda a,b: a-b)(2,5)  # 3
chain(lambda x: x+1, lambda x: x*2)(3)  # 8

### 6. Iterables / Flow

#Looping through each element
each([1,2,3]).do(print)

Conditional execution
ifit(5 > 3).then(lambda: print("Yes!"))

While loop with condition function
x = 0
whileit(lambda: x < 3).do(lambda: (print(x), globals().update(x=x+1)))

Looping sugar
with looping(n=3) as i:
    print(i)  # Prints 0, 1, 2

x = 0
with looping(cond=lambda: x < 2) as _:
    print(x)
    x += 1
### 7. Misc Utilities

swap(1,2)      # (2,1)
rangeit(5)     # [0,1,2,3,4]
lenit([1,2,3]) # 3

### Installation
Simply download my_sugar.py and place it in your project folder:

from my_sugar import *
No external dependencies required.

### Philosophy
This library is designed for beginners and anyone who wants Python code to read more like a “mini-language” shorthand. It emphasizes simplicity, readability, and playful coding.
