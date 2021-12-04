import sys


def get_input():
  with open("input", "r") as filey:
    for line in filey:
      yield line


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
