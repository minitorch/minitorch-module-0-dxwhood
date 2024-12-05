"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1

#
# Implementation of a prelude of elementary functions.


# Mathematical functions:
# - mul
def mul(x: float, y: float) -> float:
    return x * y


# - id
def id(x: float) -> float:
    return x


# - add
def add(x: float, y: float) -> float:
    return x + y


# - neg
def neg(x: float) -> float:
    return -x


# - lt
def lt(x: float, y: float) -> bool:
    return x < y


# - eq
def eq(x: float, y: float) -> bool:
    return x == y


# - max
def max(x: float, y: float) -> float:
    return y if lt(x, y) else x


# - is_close
def is_close(x: float, y: float) -> bool:
    return abs(x - y) <= 0.01


# - sigmoid
def sigmoid(x: float) -> float:
    if x >= 0:
        return 1.0 / (1.0 + math.e ** (-x))
    else:
        return math.e**x / (1.0 + math.e**x)


# - relu
def relu(x: float) -> float:
    if x >= 0:
        return x
    else:
        return 0


# - log
def log(x: float) -> float:
    return math.log(x)


# - exp
def exp(x: float) -> float:
    return math.e**x


# - log_back
def log_back(x: float, d: float) -> float:
    return d * (1 / x)


# - inv
def inv(x: float) -> float:
    return 1 / x


# - inv_back
def inv_back(x: float, d: float) -> float:
    return -d / (x**2)


# - relu_back
def relu_back(x: float, d: float) -> float:
    return d if x > 0 else 0


#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#


# Use these to implement
# - negList : negate a list
def negList(a: list) -> list:
    return a


# - addLists : add two lists together
def addLists(a: list, b: list) -> list:
    return a + b


# - sum: sum lists
def sum(a: list) -> float:
    return a[0]


# - prod: take the product of lists
def prod(a: list) -> float:
    return a[0]


# TODO: Implement for Task 0.3.
