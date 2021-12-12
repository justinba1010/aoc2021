import sys

from functools import reduce

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))


def get_input():
  with open("input", "r") as filey:
    for line in filey:
      yield line.strip()


def transformed_input():
  return [lmap(int, line.strip()) for line in get_input()]


def get_neighbors(i, j, matrix):
  positions = [
      (i + ii, j + ij) for (ii, ij) in [(1, 0), (-1, 0), (0, 1), (0, -1)]
  ]
  rowl, coll = len(matrix), len(matrix[0])
  return lfilter(
      lambda x: x[0] >= 0 and x[0] < rowl and x[1] >= 0 and x[1] < coll,
      positions)


def min_points(matrix):
  min_points = []
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      neighbors = get_neighbors(i, j, matrix)
      neighbor_values = lmap(lambda x: matrix[x[0]][x[1]], neighbors)
      if matrix[i][j] < min(neighbor_values):
        min_points.append((i, j))
  return min_points


def solution():
  matrix = transformed_input()
  return sum(lmap(lambda x: matrix[x[0]][x[1]] + 1, min_points(matrix)))


if __name__ == "__main__":
  print(solution())
