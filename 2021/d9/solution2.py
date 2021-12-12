from aocd import get_data
import sys

from functools import reduce

DEBUG = False

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))


def get_input():
  return get_data(day=9).split("\n")


def transformed_input():
  return [lmap(int, line.strip()) for line in get_input()]


def basin_search(matrix, start_i, start_j, covered):
  stack = [(start_i, start_j)]
  basin = []
  value = lambda x: matrix[x[0]][x[1]]
  on_map = lambda x: x[0] >= 0 and x[0] < len(matrix) and x[1] >= 0 and x[
      1] < len(matrix[0])
  while stack:
    curr = stack.pop()
    if value(curr) < 9 and curr not in covered:
      basin.append(curr)
    else:
      continue
    covered.add(curr)
    (i, j) = curr
    candidates = [
        (i + ii, j + ij) for (ii, ij) in [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ]
    candidates = lfilter(on_map, candidates)
    candidates = lfilter(lambda x: x not in covered, candidates)
    stack += candidates
  return basin


def view_basins(basins, matrix):
  my_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
  for index, basin in enumerate(basins):
    for (i, j) in basin:
      my_matrix[i][j] = index + 1
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      print(my_matrix[i][j], end="")
    print("")


def find_all_basins(matrix):
  covered = set()
  basins = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if (i, j) not in covered:
        basin = basin_search(matrix, i, j, covered)
        if basin:
          basins.append(basin)
  if DEBUG:
    view_basins(basins, matrix)
  return basins


def solution():
  matrix = transformed_input()
  mul = lambda acc, x: acc * x
  basin_lengths = lmap(len, find_all_basins(matrix))
  return reduce(mul, sorted(basin_lengths, reverse=True)[:3], 1)


if __name__ == "__main__":
  print(solution())
