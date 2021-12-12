from aocd import get_data
import sys

from functools import reduce

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))


def get_input():
  return get_data(day=8).split("\n")


def transformed_input():
  first_halves, second_halves = [], []
  for line in get_input():
    split = lambda x: x.strip().split(" ")
    first_half, second_half = line.split("|")
    first_halves.append(first_half)
    second_halves.append(second_half)
  return first_halves, second_halves


def solution():
  s = transformed_input()[1]
  s = map(lambda x: x.split(" "), s)
  s = [i for x in s for i in x]
  return len(lfilter(lambda x: len(x) in [2, 4, 3, 7], s))


if __name__ == "__main__":
  print(solution())
