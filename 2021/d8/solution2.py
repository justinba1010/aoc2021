from aocd import get_data
import sys

from functools import reduce
from collections import Counter

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))

nums = [
    "abcefg",  #0
    "cf",  #1
    "acdeg",  #2
    "acdfg",  #3
    "bcdf",  #4
    "abdfg",  #5
    "abdefg",  #6
    "acf",  #7
    "abcdefg",  #8
    "abcdfg",  #9
]


def get_input():
  return get_data(day=8).split("\n")


def transformed_input():
  first_halves, second_halves = [], []
  for line in get_input():
    split = lambda x: x.strip().split(" ")
    first_half, second_half = line.split("|")
    first_halves.append(split(first_half))
    second_halves.append(split(second_half))
  return first_halves, second_halves


def solution():
  sum = 0
  for first_half, second_half in zip(*transformed_input()):
    """
    0 -> 6
    1 -> 2
    2 -> 5
    3 -> 5
    4 -> 4
    5 -> 5
    6 -> 6
    7 -> 3
    8 -> 7
    9 -> 6
    """
    one = set(lfilter(lambda x: len(x) == 2, first_half)[0])
    four = set(lfilter(lambda x: len(x) == 4, first_half)[0])
    seven = set(lfilter(lambda x: len(x) == 3, first_half)[0])
    eight = set(lfilter(lambda x: len(x) == 7, first_half)[0])
    two, three, five = lfilter(lambda x: len(x) == 5, first_half)
    count_235 = Counter(two + three + five)
    two_three_five = set(list(two) + list(three) + list(five))
    zero, six, nine = lfilter(lambda x: len(x) == 6, first_half)
    count_069 = Counter(zero + six + nine)

    A = set(seven) - set(one)
    BE = set([k for (k, v) in count_235.items() if v == 1])
    DCE = set([k for (k, v) in count_069.items() if v == 2])
    E = BE.intersection(DCE)
    B = BE - E
    DC = DCE - E
    G = set(eight) - set(four) - A - DCE
    D = DC - set(one)
    C = DC - D
    F = set(eight) - A - B - C - D - E - G

    mappy = lmap(lambda x: list(x)[0], [A, B, C, D, E, F, G])
    num = 0
    for number in second_half:
      num *= 10
      new_letters = [mappy.index(i) for i in number]
      new_letters = "".join(map(lambda x: nums[8][x], new_letters))
      new_letters = "".join(sorted(new_letters))
      num += nums.index(new_letters)
    sum += num
  return sum

  # Get Map from first halves
  # Get value from second halves


if __name__ == "__main__":
  print(solution())
