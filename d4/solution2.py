import sys

from functools import reduce


def get_input():
  with open("input", "r") as filey:
    for line in filey:
      yield line.strip()


def transformed_input():
  inp = list(get_input())
  nums = list(map(int, inp.pop(0).strip().split(",")))
  matrices = []
  while inp:
    matrix = []
    inp.pop(0)
    for _ in range(5):
      matrix.append(
          list(
              map(int,
                  filter(lambda x: x.isdigit(),
                         inp.pop(0).strip().split(" ")))))
    matrices.append(matrix)
  return nums, matrices


def winner(nums, matrix):
  bools = [[matrix[i][j] in nums for j in range(5)] for i in range(5)]
  for i in range(5):
    # Check horizontals
    if all((bools[i][j] for j in range(5))):
      return True
    # Check verticals
    if all((bools[j][i] for j in range(5))):
      return True
  # Check diagonals
  # Nevermind
  """
  if all((bools[i][4-i] for i in range(5))):
    return True
  if all((bools[4-i][i] for i in range(5))):
    return True
  """
  return False


def calc(nums, matrix):
  vals = [matrix[i][j] for i in range(5) for j in range(5)]
  left = list(filter(lambda x: x not in nums, vals))
  return (sum(left))


def solution():
  (nums, matrices) = transformed_input()
  for i in range(len(nums) - 1, -1, -1):
    for matrix in matrices:
      if not winner(nums[:i], matrix):
        val = calc(nums[:i + 1], matrix)
        return val * nums[i]


if __name__ == "__main__":
  print(solution())
