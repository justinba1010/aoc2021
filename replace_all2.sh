#!/usr/bin/env sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"


for i in {1..12}; do
  echo $i
  git checkout HEAD~2 -- d$i/solution.py d$i/solution2.py
  git checkout HEAD~2 -- d$i/solution1.py
  mv d$i/solution.py 2021/d$i/
  mv d$i/solution1.py 2021/d$i/
  mv d$i/solution2.py 2021/d$i/
done
