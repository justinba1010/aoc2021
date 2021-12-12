from aocd import get_data
import sys

from functools import reduce

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))


def get_input():
  return get_data(day=6).split("\n")


def transformed_input():
  return lmap(int, next(get_input()).split(","))


def solution():
  lantern_fish = transformed_input()
  days = [len(lfilter(lambda x: x == i, lantern_fish)) for i in range(9)]

  def next_day(days, _):
    fish_spawning_day_i = days.pop(0)
    # Reset todays fish
    days[6] += fish_spawning_day_i
    # Spawn new fish
    days.append(fish_spawning_day_i)
    return days

  return sum(reduce(next_day, range(256), days))


if __name__ == "__main__":
  print(solution())
