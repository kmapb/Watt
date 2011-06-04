#!/usr/bin/python

import unicodedata

"""
Module for tokenizing strings.
"""

def normalize_line(s):
  return unicodedata.normalize('NFD', s.lower())

def normalize_token(s):
  return unicodedata.normalize('NFC', s)

def tokenorm(line):
  tokens = []
  token = ''
  # Poor man's accent stripping: normalize to Unicode NFD
  # and strip out values with category Mark (accents))
  for c in normalize_line(line.decode('utf-8', 'replace')):
    cat = unicodedata.category(c)
    if cat.startswith('L') or cat.startswith('N'):
      # Letters and numbers come through.
      token += c
    elif cat.startswith('M'):
      # Accents and other marks are ignored.
      pass
    elif len(token) > 0:
      # Anything else is assumed to be a separator.
      tokens.append(normalize_token(token))
      token = ''

  if len(token) > 0:
    tokens.append(normalize_token(token))

  return tokens

