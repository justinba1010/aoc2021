import aocd
import sys

from collections import defaultdict, Counter
from functools import reduce

DEBUG = False

# Eager evaluation makes this easier
lmap = lambda x, y: list(map(x, y))
lfilter = lambda x, y: list(filter(x, y))
tzip = lambda *x: list(zip(x))


def get_input():
  if len(sys.argv) == 1:
    return aocd.get_data(day=14).split("\n")
  else:
    with open("input", "r") as filey:
      return lmap(lambda x: x.strip(), filey)


def transformed_input():
  g = get_input()
  return g[0], lmap(lambda x: tuple(x.split(" -> ")), g[2:])


def make_map(subs):
  return {x[0]: x[1] for x in subs}


def turn(string_pairs, dictionary, char_count):
  for (x, y), count in list(string_pairs.copy().items())[:]:
    key = dictionary.get(x + y)
    if DEBUG:
      print(key)
    if not key:
      continue
    string_pairs[(x, y)] -= count
    string_pairs[(x, key)] += count
    string_pairs[(key, y)] += count
    char_count[key] += count


def solution():
  string, dictionary = transformed_input()
  dictionary = make_map(dictionary)
  string_pairs = zip(list(string), list(string[1:]))
  if DEBUG:
    print("String Pairs: ", string_pairs)
  count = Counter(list(string))
  if DEBUG:
    print(count)
  pair_counter = Counter(string_pairs)
  if DEBUG:
    print("Pair Counter: ", pair_counter)
  for i in range(40):
    turn(pair_counter, dictionary, count)
    if DEBUG:
      print("Pair Counter: ", pair_counter)
    if DEBUG:
      print("Count: ", count)
  count += Counter()
  if DEBUG:
    print("Count: ", count)
  return count.most_common()[0][1] - count.most_common()[-1][1]


if __name__ == "__main__":
  print(solution())
"""
abcd
ab -> e
bc -> f
cd -> g

Start
[ab] = 1
[bc] = 1
[cd] = 1

[ab]--
[ae]++
[eb]++
...


ababab
ab -> c
ba -> d
acbdacbdacb
[ab] = 3
[ba] = 2
[ab] -= 3
[ac] += 3
[cb] += 3
[bd] += 2
[da] += 2



"""
