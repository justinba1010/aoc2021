import aocd
import sys

from collections import defaultdict, Counter
from functools import reduce

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))


def get_input():
  if len(sys.argv) == 1:
    return aocd.get_data(day=15).split("\n")
  else:
    with open("input", "r") as filey:
      return lmap(lambda x: x.strip(), filey)


def transformed_input():
  return lmap(lambda x: lmap(int, list(x)), get_input())


def solution():
  """
  Simple dynamic programming
  lol misread the problem, says diagonally not left and up....
  """
  costs = transformed_input()
  matrix = [[0 for _ in range(len(costs[0]))] for __ in range(len(costs))]
  # Fill the first row and column
  matrix[0][0] = costs[0][0]
  for i in range(1, len(matrix)):
    matrix[i][0] = matrix[i - 1][0] + costs[i][0]
  for i in range(1, len(matrix[0])):
    matrix[0][i] = matrix[0][i - 1] + costs[0][i]

  # Dynamic programming part
  for i in range(1, len(costs)):
    for j in range(1, len(costs[0])):
      matrix[i][j] = min(matrix[i][j - 1], matrix[i - 1][j]) + costs[i][j]
  #return matrix[-1][-1]
  return "\n\n".join(lmap(lambda x: "\t".join(lmap(str, x)), matrix))


if __name__ == "__main__":
  print(solution())
