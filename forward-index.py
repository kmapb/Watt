#!/usr/bin/python

# Output a crude forward index given a directory.

if len(sys.argv) < 1:
  sys.stderr.write("usage: index.py /path/to/directory")
  sys.exit(1)

def splitNormalizeAndStrip(line):
  punctuation = '!@#$%^&*()-_+=`~{}[]|\\\'";:/?<>,.'
  for p in punctuation:
    line.replace(p, ' ')
  return line.lower.split()

def indexFile(path):
  f = open(path)
  tokensSeen = { }
  for line in f:
    tokens = splitNormalizeAndStrip(line)
    for tok in tokens:
      tokensSeen[tok] = True
  return (path, tokensSeen)

dict = { }
(path, tokensSeen) = indexFile(sys.argv[0])
dict[path] = tokensSeen
print dict
