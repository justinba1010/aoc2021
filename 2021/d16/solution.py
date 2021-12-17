import aocd
import sys

from collections import defaultdict, Counter
from functools import reduce

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))

def tobinarr(byte):
  x = lmap(int, bin(byte)[2:])
  while len(x) < 8:
    x = [0] + x
  return x


def get_input():
  if len(sys.argv) == 1:
    return aocd.get_data(day=15).split("\n")
  else:
    with open("input", "r") as filey:
      return lmap(lambda x: x.strip(), filey)


def transformed_input():
  return reduce(lambda acc, x: acc + tobinarr(x), (byte for byte in bytes.fromhex(get_input()[0])), [])

def to_int(arr):
  if arr == []:
    raise Exception("Sad")
  return int("".join(map(str,arr)),2)

def decode_instruction(instructions):
  instructions = instructions[:]
  try:
    version, instructions = to_int(instructions[:3]), instructions[3:]
    type_, instructions = to_int(instructions[:3]), instructions[3:]
  except:
    return instructions, 0, 0, "Sad :("
  match type_:
    case 4:
      # Value
      curr = 16
      value = 0
      while curr >= 16:
        try:
          curr, instructions = to_int(instructions[:5]), instructions[5:]
        except:
          return instructions, 0, 0, "Sad :("
        value <<= 4
        value += curr & 15
      return instructions[:], version, type_, value
    case _:
      try:
        i, instructions = to_int(instructions[:1]), instructions[1:]
      except:
        return instructions, 0, 0, "Sad :("
      match i:
        case 0:
          try:
            l, instructions = to_int(instructions[:15]), instructions[15:]
          except:
            return instructions, 0, 0, "Sad :("
          new_instructions, instructions = instructions[:l][:], instructions[l:]
          children = []
          while new_instructions:
            new_instructions, version_, type__, value_ = decode_instruction(new_instructions)
            child = (version_, type__, value_)
            children.append(child)
          return instructions[:], version, type_, children
        case 1:
          try:
            l, instructions = to_int(instructions[:11]), instructions[11:]
          except:
            return instructions, 0, 0, "Sad :("
          children = []
          for i in range(l):
            instructions, version_, type__, value_ = decode_instruction(instructions)
            child = (version_, type__, value_)
            children.append(child)
          return instructions[:], version, type_, children

def solution1_tree(tree):
  match tree:
    case (version, 4, value):
      return version
    case (version, type_, children):
      return version + sum(lmap(solution1_tree, children))


def solution():
  bit_stream = transformed_input()
  d, *x = decode_instruction(bit_stream)
  return x
  return solution1_tree(x)
  return transformed_input()


if __name__ == "__main__":
  print(solution())
