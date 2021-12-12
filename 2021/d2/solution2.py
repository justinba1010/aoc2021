"""
Requires Python >3.10
"""

from aocd import get_data
import sys

from functools import reduce

def get_input():
  return get_data(day=2).split("\n")

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
