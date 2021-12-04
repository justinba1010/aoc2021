import sys

from functools import reduce


def get_input():
  with open("input", "r") as filey:
    for line in filey:
      yield line.strip()


def get_most_common(nums):
  if nums is []:
    return []
  vals = list(zip(*nums))
  return list(
      map(lambda x: 0 if x < 0 else 1,
          [sum(map(lambda x: -1 if x == 0 else 1, val)) for val in vals]))


calc = lambda x: reduce(lambda acc, y: acc * 2 + y, x)


def solution():
  oxygens = list(map(lambda x: list(map(int, (i for i in x))), get_input()))
  carbons = list(map(lambda x: list(map(int, (i for i in x))), get_input()))
  index = 0
  oxygen = 0
  carbon = 0
  # Annoying, lambdas got me in trouble here
  while True:
    if len(oxygens) == 1:
      oxygen = calc(oxygens.pop())
      break
    o = get_most_common(oxygens)[index]
    oxygens = list(filter(lambda x: x[index] == o, oxygens))
    index += 1
  index = 0
  while True:
    if len(carbons) == 1:
      carbon = calc(carbons.pop())
      break
    c = get_most_common(carbons)[index] + 1
    c %= 2
    carbons = list(filter(lambda x: x[index] == c, carbons))
    index += 1
  return oxygen * carbon


if __name__ == "__main__":
  print(solution())
