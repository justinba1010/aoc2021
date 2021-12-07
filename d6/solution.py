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


def day(lantern_fish):
  next_day = lmap(lambda x: x - 1, lantern_fish)
  zeroes = len(lfilter(lambda x: x == -1, next_day))
  next_day = lmap(lambda x: x if x != -1 else 6, next_day)
  next_day += [8] * zeroes
  return next_day


def solution():
  lantern_fish = transformed_input()
  for i in range(80):
    lantern_fish = day(lantern_fish)
  return len(lantern_fish)


if __name__ == "__main__":
  print(solution())
