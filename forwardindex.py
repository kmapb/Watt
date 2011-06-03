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
    tokens = tokenize.tokenorm(line)
    for tok in tokens:
      tokensSeen |= set([tok])
  return tokensSeen

def filesInPath(p):
  # BFS on the provided path to generate all enclosed files
  frontier = [ p ]
  while frontier:
    path = frontier.pop()
    if os.path.isdir(path):
      frontier += [ os.path.join(path, p) for p in os.listdir(path) ]
    else:
      yield path

forwardIndex = { }
for path in filesInPath(sys.argv[1]):
  if not (path.endswith(".zip") or path.endswith(".mp4") or
    path.endswith(".jpg") or path.endswith(".png") or
    path.endswith(".mp3")):
    forwardIndex[path] = indexFile(path)

pickle.dump(forwardIndex, sys.stdout)

