#!/usr/bin/python

import sys
import os
import pickle

# Read a pickled forward index from stdin, and produce
# pickled reverse index on stdout.
forwardIndex = pickle.load(sys.stdin)

# forward index maps pathnames to tokens; reverseIndex will
# map terms to pathnames.
reverseIndex = { }
for path in forwardIndex.keys():
  for term in forwardIndex[path]:
    reverseIndex.setdefault(term, []).append(path)

pickle.dump(reverseIndex, sys.stdout)

