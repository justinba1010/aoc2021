from aocd import get_data
import sys

from functools import reduce


def get_input():
  return get_data(day=3).split("\n")


def solution():
  positions = list(
      zip(*list(
          map(
              lambda x: list(
                  map(lambda y: 1 if y == "1" else -1, (i for i in x))),
              get_input()))))
  sums = map(sum, positions)
  epsilon = reduce(lambda acc, x: acc * 2 + (1 if x > 0 else 0), sums, 0)
  # cheaty
  n = len(next(get_input()))
  return (2**n - 1 - epsilon) * epsilon


if __name__ == "__main__":
  print(solution())
