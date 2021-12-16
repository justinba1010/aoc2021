import aocd
import sys

from collections import defaultdict, Counter
from functools import reduce

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))


def get_input():
  if len(sys.argv) == 1:
    return aocd.get_data(day=14).split("\n")
  else:
    with open("input", "r") as filey:
      return lmap(lambda x: x.strip(), filey)


def transformed_input():
  g = get_input()
  return g[0], lmap(lambda x: tuple(x.split(" -> ")), g[2:])


def make_map(subs):
  return {x[0]: x[1] for x in subs}


def turn(string, dictionary):
  new_string = ""
  for i in range(len(string)):
    new_string += string[i]
    new_string += " " if string[i:i + 2] not in dictionary else dictionary[
        string[i:i + 2]]
  return new_string


def solution():
  string, dictionary = transformed_input()
  dictionary = make_map(dictionary)
  string = reduce(lambda acc, _: turn(acc, dictionary), range(10), string)
  counter = Counter(string)
  return counter.most_common()[0][1] - counter.most_common()[-1][1]


if __name__ == "__main__":
  print(solution())
