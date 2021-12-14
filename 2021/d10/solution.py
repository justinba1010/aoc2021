import sys

from functools import reduce

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))


def get_input():
  with open("input", "r") as filey:
    for line in filey:
      yield line.strip()


def transformed_input():
  return lmap(list, get_input())


maps = {'[': ']', '(': ')', '{': '}', '<': '>'}
values = {')': 3, ']': 57, '}': 1197, '>': 25137}


def get_malformed(lines):
  for line in lines:
    stack = []
    while line:
      char = line.pop(0)
      if char in maps.keys():
        stack.append(char)
      elif stack:
        if char != maps[stack[-1]]:
          yield char
          break
        if char == maps[stack[-1]]:
          stack.pop()
      else:
        # Technically malformed
        pass


def reformed(stack):
  stack.reverse()
  return lmap(lambda x: maps[x], stack)


def solution():
  lines = transformed_input()
  malformeds = list(get_malformed(lines))
  return sum(map(lambda x: values[x], malformeds))


if __name__ == "__main__":
  print(solution())
