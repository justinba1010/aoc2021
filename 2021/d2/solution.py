from aocd import get_data
import sys


def get_input():
  return get_data(day=2).split("\n")


def solution():
  commands = list(
      map(lambda x: (x[0], int(x[1])), map(lambda x: x.split(" "),
                                           get_input())))
  horizontals = sum(
      map(lambda x: x[1], filter(lambda x: x[0] == "forward", commands)))
  ups = sum(map(lambda x: x[1], filter(lambda x: x[0] == "up", commands)))
  downs = sum(map(lambda x: x[1], filter(lambda x: x[0] == "down", commands)))
  return horizontals * (downs - ups)


if __name__ == "__main__":
  print(solution())
