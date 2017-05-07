#!/bin/bash

ls ../src/*.md | while read i; do

echo "Headlines in: $i"
grep  "^\#" "../src/$i"
done
