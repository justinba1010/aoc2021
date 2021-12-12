#!/usr/bin/env sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"


for i in {1..12}; do
  echo $i
  ./replace.py $SCRIPT_DIR/d$i/solution.py $i || true
  ./replace.py $SCRIPT_DIR/d$i/solution1.py $i || true
  ./replace.py $SCRIPT_DIR/d$i/solution2.py $i || true
done
