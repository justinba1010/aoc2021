"""
Requires Python >3.10
"""

import sys

from functools import reduce

def get_input():
  with open("input", "r") as filey:
    for line in filey:
      yield line

def acc_func(acc, command):
  (horizontal, depth, aim) = acc
  match command:
    case ("forward", x):
      return (horizontal + x, depth + aim * x, aim)
    case ("up", x):
      return (horizontal, depth, aim - x)
    case ("down", x):
      return (horizontal, depth, aim + x)
  

def solution():
  commands = map(lambda x: (x[0], int(x[1])), map(lambda x: x.split(" "), get_input()))
  return (lambda x: x[0] * x[1])(reduce(acc_func, commands, (0,0,0)))


if __name__ == "__main__":
  print(solution())
