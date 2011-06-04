#!/usr/bin/python

import sys
import os
import pickle
import tokenize

# Output a crude forward index given a directory.

if len(sys.argv) < 2:
  sys.stderr.write("usage: forwardindex.py /path/to/directory\n")
  sys.exit(1)

def indexFile(path):
  f = open(path)
  tokensSeen = set([])
  for line in f:
    u = line.decode('utf-8', 'replace')
    tokens = tokenize.tokenorm(u)
    for tok in tokens:
      tokensSeen |= set([tok])
  return tokensSeen

forwardIndex = { }

for root, dirs, files in os.walk(sys.argv[1]):
  for path in files:
    if not (path.endswith(".zip") or path.endswith(".mp4") or
            path.endswith(".jpg") or path.endswith(".png") or
            path.endswith(".mp3")):
      fullPath = os.path.join(root, path)
      forwardIndex[fullPath] = indexFile(fullPath)

pickle.dump(forwardIndex, sys.stdout)

