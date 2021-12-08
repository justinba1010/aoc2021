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
  return lmap(int, next(get_input()).split(","))


def distances(i, whales):
  return sum(
      map(
          lambda x: (x**2 + x) // 2,
          map(lambda x: abs(x[0] - x[1]),
              zip(whales, (i for _ in range(len(whales)))))))


def solution():
  whales = transformed_input()
  whales.sort()
  l = len(whales)
  search_space = list(range(l // 2 - l // 4, l // 2 + l // 4))
  min = float("inf")
  for i in search_space:
    current = distances(i, whales)
    if current < min:
      min = current

  return min


if __name__ == "__main__":
  print(solution())
