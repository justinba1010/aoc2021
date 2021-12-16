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


def sg(matrix, i, j):
  if i < len(matrix) and j < len(matrix[0]):
    return matrix[i][j]
  return 2**32


def neighborhood(matrix, i, j):
  return lfilter(
      lambda x: x[0] < len(matrix) and x[0] >= 0 and x[1] < len(matrix[0]
                                                               ) and x[1] >= 0,
      ((x + i, y + j) for (x, y) in [(0, 1), (1, 0), (0, -1), (-1, 0)]))


def solution():
  """
  Pathfinding
  """
  costs = transformed_input()
  matrix = [[2**32 for _ in range(len(costs[0]))] for __ in range(len(costs))]
  matrix[0][0] = 0
  visited = Counter()
  stack = [(0, 0)]
  while stack:
    (i, j) = stack.pop(0)
    neighbors = neighborhood(matrix, i, j)
    visited[(i, j)] += 1
    cheapest_neighbor = min(lmap(lambda x: sg(matrix, x[0], x[1]), neighbors))
    matrix[i][j] = min(matrix[i][j], cheapest_neighbor + costs[i][j])
    stack += lfilter(lambda x: visited[x] < 4 and x not in stack, neighbors)
  return matrix[-1][-1]
  return "\n\n".join(lmap(lambda x: "\t".join(lmap(str, x)), matrix))


if __name__ == "__main__":
  print(solution())
