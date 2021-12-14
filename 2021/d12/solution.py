import sys

from collections import defaultdict
from functools import reduce

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))


def get_input():
  with open("input", "r") as filey:
    for line in filey:
      yield line.strip()


def transformed_input():
  return lmap(lambda x: (x[0], x[1]), map(lambda x: x.split("-"), get_input()))

def lazy_path(graph, current, target, path):
  for neighbor in graph[current]:
    if neighbor == target:
      yield path[:] + [target]
    elif neighbor in path and neighbor.islower():
      pass
    else:
      yield from lazy_path(graph, neighbor, target, path + [neighbor])


def make_graph(edges):
  G = defaultdict(list)
  for (v1, v2) in edges:
    G[v1].append(v2)
    G[v2].append(v1)
  paths = list(lazy_path(G, 'start', 'end', ['start']))
  return len(paths)

def solution():
  edges = transformed_input()
  G = make_graph(edges)
  return G


if __name__ == "__main__":
  print(solution())
