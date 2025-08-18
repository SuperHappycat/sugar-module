# my_sugar.py
# Mini Python shorthand library
# Author: Your Name
# Version: 1.0

from contextlib import contextmanager
from functools import reduce

# -------------------
# 2. Print multiple times
# -------------------
def printn(text, n=1):
    for _ in range(n):
        print(text)

# -------------------
# 3. Math
# -------------------
def add(*args): return sum(args)
def mul(*args):
    result = 1
    for x in args:
        result *= x
    return result
def sq(x): return x*x
def cube(x): return x*x*x
def maxit(*args): return max(args)
def minit(*args): return min(args)
def reduceit(iterable, func, start=None):
    return reduce(func, iterable, start) if start is not None else reduce(func, iterable)

# -------------------
# 4. String
# -------------------
def repeat(s, n): return s*n

# -------------------
# 5. Boolean
# -------------------
def yes(): return True
def no(): return False

# -------------------
# 6. Function utilities
# -------------------
def short(func):
    """Decorator: prints running function name"""
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

def flip(func):
    """Reverse args of a function"""
    return lambda *args: func(*reversed(args))

def chain(*funcs):
    """Chain multiple functions"""
    def inner(val):
        for f in funcs:
            val = f(val)
        return val
    return inner

# -------------------
# 7. Iterables / Flow
# -------------------
class Each:
    def __init__(self, iterable):
        self.iterable = iterable
    def do(self, func):
        for i in self.iterable:
            func(i)
def each(iterable):
    return Each(iterable)

class IfIt:
    def __init__(self, cond):
        self.cond = cond
    def then(self, func):
        if self.cond:
            func()
def ifit(cond):
    return IfIt(cond)

class WhileIt:
    def __init__(self, cond_func):
        self.cond_func = cond_func
    def do(self, func):
        while self.cond_func():
            func()
def whileit(cond_func):
    return WhileIt(cond_func)

# -------------------
# 8. Misc
# -------------------
def swap(a,b): return b,a
def rangeit(*args): return list(range(*args))
def lenit(obj): return len(obj)

