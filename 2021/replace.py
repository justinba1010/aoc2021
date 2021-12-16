#!/usr/bin/env python3
import sys

newfile = ""

removes = [
    "def get_input()", "with open(\"input\"", "for line in filey", "yield line"
]

d = "from aocd import get_data"
replace = lambda day: "def get_input():\n  return get_data(day=%s).split(\"\\n\")" % day

with open(sys.argv[1], "r") as filey:
  for line in filey:
    if "import sys" in line:
      newfile += d + "\n"
      newfile += line
    elif any(map(lambda x: x in line, removes)):
      if removes[0] in line:
        newfile += replace(sys.argv[2]) + "\n"
    else:
      newfile += line
with open(sys.argv[1], "w") as filey:
  filey.write(newfile)
