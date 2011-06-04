#!/usr/bin/python

import sys
import os
import pickle
import tokenize

if len(sys.argv) < 2:
  sys.stderr.write("usage: query.py <reverseindex>\n")
  sys.exit(1)

reverseIndex = pickle.load(open(sys.argv[1], 'r'))

def queryReverseIndex(ri, q):
  if not q in ri:
    return set([])
  return set(reverseIndex[q])

for line in sys.stdin:
  u = line.decode('utf-8', 'replace')
  query = tokenize.tokenorm(u)
  if query:
    docs = queryReverseIndex(reverseIndex, query.pop())
    while query:
      docs.intersection_update(queryReverseIndex(reverseIndex,
                                                 query.pop()))
  print line
  for doc in docs:
    print "%80s" % (doc)

