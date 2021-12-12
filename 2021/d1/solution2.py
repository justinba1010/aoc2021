import sys


def get_input():
  with open("input", "r") as filey:
    for line in filey:
      yield line


def solution():
  nums = list(map(lambda x: int(x.strip()), get_input()))
  nums = list(map(sum, zip(nums, nums[1:], nums[2:])))
  return len(list(filter(lambda x: x[0] < x[1], zip(nums, nums[1:]))))


if __name__ == "__main__":
  print(solution())
