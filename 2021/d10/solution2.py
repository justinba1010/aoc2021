from aocd import get_data
import sys

from functools import reduce

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))


def get_input():
  return get_data(day=10).split("\n")


def transformed_input():
  return lmap(list, get_input())


maps = {'[': ']', '(': ')', '{': '}', '<': '>'}
values = {')': 1, ']': 2, '}': 3, '>': 4}


def get_malformed(lines):
  for line in lines:
    stack = []

    # https://stackoverflow.com/questions/2597104/break-the-nested-double-loop-in-python
    try:
      while line:
        char = line.pop(0)
        if char in maps.keys():
          stack.append(char)
        elif stack:
          if char != maps[stack[-1]]:
            raise Exception("Hi")
          if char == maps[stack[-1]]:
            stack.pop()
        else:
          # Technically malformed
          raise Exception("Hi")
      if stack:
        yield stack
    except:
      pass


def reformed(stack):
  stack.reverse()
  return lmap(lambda x: maps[x], stack)


def solution():
  lines = transformed_input()
  malformeds = list(get_malformed(lines))
  corrections = lmap(reformed, malformeds)
  return sorted(lmap(score, corrections))[len(corrections) // 2]


def score(reform):
  return reduce(lambda acc, x: acc * 5 + values[x], reform, 0)


if __name__ == "__main__":
  print(solution())
