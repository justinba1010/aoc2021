import aocd
import sys

from collections import defaultdict
from functools import reduce

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))


def get_input():
  if len(sys.argv) == 1:
    return aocd.get_data(day=13).split("\n")
  else:
    with open("input", "r") as filey:
      return lmap(lambda x: x.strip(), filey)


def transformed_input():
  nums = []
  directions = []
  for line in get_input():
    if len(line) == 0:
      continue
    elif line[0] != 'f':
      nums.append(line)
    else:
      directions.append(line)
  new_directions = []
  for direction in directions:
    yx, num = direction.split("=")
    yx = 'y' if yx.endswith('y') else 'x'
    new_directions.append((yx, int(num)))

  return lmap(lambda x: (int(x[1]), int(x[0])), map(lambda x: x.split(","),
                                                    nums)), new_directions


get_maxi = lambda spots: max(map(lambda x: x[0], spots))
get_maxj = lambda spots: max(map(lambda x: x[1], spots))


def sg(matrix, i, j):
  if len(matrix) > i and len(matrix[0]) > j:
    return matrix[i][j]
  return 0


def merge_top(top, bottom):
  maxi = max(len(top), len(bottom))
  maxj = max(len(top[0]), len(bottom[0]))
  matrix_top = [[sg(top, i, j) for j in range(maxj)] for i in range(maxi)]
  return [[sg(bottom, maxi - i - 1, j) | matrix_top[i][j]
           for j in range(maxj)]
          for i in range(maxi)]


def fold_top(matrix, rows):
  top = matrix[:rows][:]
  bottom = matrix[rows + 1:][:]
  return merge_top(top, bottom)


def fold_left(matrix, columns):
  left = [matrix[i][:columns][:] for i in range(len(matrix))]
  right = [matrix[i][columns + 1::][:] for i in range(len(matrix))]
  raise Exception("Fuck you")
  return mer(left, right)


def pretty_print(matrix):
  for row in matrix:
    for column in row:
      print('#' if column == 1 else '.', end="")
    print()
  print()


def solution():
  spots, directions = transformed_input()
  print("Spots", spots)
  print("Directions", directions)
  maxi = get_maxi(spots) + 1
  maxj = get_maxj(spots) + 1
  s = set(spots)
  matrix = [[1 if (i, j) in s else 0 for j in range(maxj)] for i in range(maxi)]
  pretty_print(matrix)
  for (xy, line) in directions:
    if xy == 'x':
      matrix = fold_left(matrix, line)
    else:
      matrix = fold_top(matrix, line)
    pretty_print(matrix)
  return sum(map(sum, matrix))


if __name__ == "__main__":
  print(solution())
