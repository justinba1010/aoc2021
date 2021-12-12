from aocd import get_data
import sys

from functools import reduce

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))


def get_input():
  return get_data(day=11).split("\n")


def transformed_input():
  return lmap(lambda x: lmap(int, x), lmap(list, get_input()))


count = 0


def step(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      matrix[i][j] = matrix[i][j] + 1
  visited = set()
  while flashes(matrix, visited):
    pass
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] > 9:
        matrix[i][j] = 0


def flashes(matrix, visited):
  global count
  neighbors_ = lambda x, y: [(i + x, j + y)
                             for i in range(-1, 2)
                             for j in range(-1, 2)]
  neighbors = lambda x, y: lfilter(
      lambda y: y[0] >= 0 and y[0] < len(matrix) and y[1] >= 0 and y[1] < len(
          matrix[y[0]]), neighbors_(x, y))
  flag = False
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] > 9 and (i, j) not in visited:
        count += 1
        get_neighbors = neighbors(i, j)
        get_neighbors = set(get_neighbors) - visited - set([(i, j)])
        visited.add((i, j))
        for (ni, nj) in get_neighbors:
          flag = True
          matrix[ni][nj] += 1
  return flag


def synchronized(matrix):
  return not any(
      lmap(lambda x: x != matrix[0][0], [
          matrix[i][j]
          for i in range(len(matrix))
          for j in range(len(matrix[0]))
      ]))


def solution():
  global count
  matrix = transformed_input()
  c = 0
  while not synchronized(matrix):
    c += 1
    step(matrix)
  return c


if __name__ == "__main__":
  print(solution())
