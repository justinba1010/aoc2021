from aocd import get_data
import sys


def get_input():
  return get_data(day=1).split("\n")


def solution():
  nums = list(map(lambda x: int(x.strip()), get_input()))
  return len(list(filter(lambda x: x[0] < x[1], zip(nums, nums[1:]))))


if __name__ == "__main__":
  print(solution())
