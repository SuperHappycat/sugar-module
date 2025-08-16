My_Sugar Python Library

My_Sugar is an innovative Python library that provides over 20 shorthand utilities designed to make coding faster, cleaner, and far more enjoyable. Whether you are working with loops, mathematical operations, strings, booleans, or general flow control, this library streamlines everyday tasks and reduces repetitive boilerplate code. It is especially useful for beginners who want to simplify Python syntax, as well as experienced developers looking for a lightweight productivity boost.

Installation Instructions

Clone the Repository or Download Files: Obtain the library files from GitHub or another source.

Place my_sugar.py: Ensure that the file my_sugar.py is in the same directory as your Python project for easy importing.

Import into Your Project: Use the following line in your scripts to access all shorthand utilities:

from my_sugar import *

This setup allows you to immediately start using the powerful shorthand functions included in the library.

Shorthand Utilities Overview

Loops:

with loop(n): – a context manager for repeating a block of code n times.

loop_do(n).do(func) – execute a function multiple times with minimal syntax.

Printing:

printn(text, n) – print a given text multiple times quickly and efficiently.

Mathematical Functions:

add(a, b, ...) – sum of multiple numbers.

mul(a, b, ...) – product of multiple numbers.

sq(x) – square a number.

cube(x) – cube a number.

maxit(...) – get the maximum value among arguments.

minit(...) – get the minimum value among arguments.

reduceit(iterable, func, start=None) – shorthand for applying a reduce operation on an iterable.

Strings:

repeat(s, n) – repeat a string s a specified number of times.

Booleans:

yes() – returns True.

no() – returns False.

Function Utilities:

@short – a decorator that prints a message whenever a function is executed.

flip(func) – reverses the arguments of a given function for flexible usage.

chain(func1, func2, ...) – chain multiple functions together in sequence.

Iterables and Flow Control:

each(iterable).do(func) – iterate over elements of an iterable with a concise syntax.

ifit(cond).then(func) – shorthand for conditional execution.

whileit(cond_func).do(func) – shorthand for while loops using a condition function.

Miscellaneous Utilities:

swap(a, b) – quickly swap two variable values.

rangeit(...) – shorthand version of the range function for easy iteration.

lenit(obj) – shorthand for computing the length of objects like lists, strings, or tuples.

Example Usage

from my_sugar import *

# Loops
with loop(3):
    print("Hello")

loop_do(2).do(lambda: print("World"))

# Math operations
print(add(2,3,4))        # 9
print(mul(2,3,4))        # 24
print(sq(5))              # 25
print(cube(3))            # 27

# Strings
print(repeat("Hi!", 3)) # Hi!Hi!Hi!

# Flow control
each([1,2,3]).do(lambda x: print(x*2))
ifit(5>3).then(lambda: print("Yes"))

# Booleans
print(yes())             # True
print(no())              # False

# Function decorator
@short
def greet():
    print("Greetings!")
greet()

Benefits and Use Cases

My_Sugar is perfect for learning Python, experimenting with concise coding patterns, or rapidly prototyping scripts. It reduces repetitive code, allows beginners to write clean and understandable Python, and helps experienced programmers focus on logic instead of boilerplate. Whether you are creating educational projects, automation scripts, or experimenting with new ideas, My_Sugar streamlines your workflow and encourages playful, productive coding.

The library is fully open for modification and expansion, so users can continue to add new shorthand utilities tailored to their own coding style and project needs. With My_Sugar, Python coding becomes faster, cleaner, and a lot more fun!
