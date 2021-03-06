# Source:
# https://www.reddit.com/r/adventofcode/comments/r9iy3u/2021_day_5_heatmap_of_the_vents_made_with_seaborn/

import seaborn as sns

sns.set()
import matplotlib.pyplot as plt

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
  lines = []
  transform_point = lambda x: lmap(int, x.split(","))
  for line in get_input():
    points = line.split("->")
    lines.append(lmap(transform_point, points))
  return lines


def traverse_line(matrix, line):
  start, stop = tuple(line)
  start_x, start_y = tuple(start)
  stop_x, stop_y = tuple(stop)
  vector_x = stop_x - start_x
  vector_y = stop_y - start_y
  if vector_x != 0:
    vector_x /= abs(vector_x)
  if vector_y != 0:
    vector_y /= abs(vector_y)
  # ignore non-horizontal/vertical
  if vector_x and vector_y and abs(vector_x / vector_y) != 1:
    return
  vector_x, vector_y = int(vector_x), int(vector_y)
  curr_point = (start_x, start_y)
  while curr_point != tuple(stop):
    matrix[curr_point[1]][curr_point[0]] += 1
    curr_point = (curr_point[0] + vector_x, curr_point[1] + vector_y)
  matrix[stop_y][stop_x] += 1


def solution():
  lines = transformed_input()
  max_rows = max(
      map(lambda x: x[1], (point for line in lines for point in line)))
  max_cols = max(
      map(lambda x: x[0], (point for line in lines for point in line)))
  matrix = [[0 for i in range(max_cols + 1)] for j in range(max_rows + 1)]
  for line in lines:
    traverse_line(matrix, line)

  plt.figure(figsize=(10, 10))
  ax = sns.heatmap(matrix, cbar=None, xticklabels=False, yticklabels=False)

  plt.savefig("vents.png", bbox_inches='tight', dpi=1000)


if __name__ == "__main__":
  print(solution())
