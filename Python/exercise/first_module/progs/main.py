# import sys

from sys import path
from Python.exercise.first_module.modules import module


# for p in sys.path:
#     print(p)

path.append('..\\modules')

zeroes = [0 for i in range(5)]
ones = [1 for j in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
