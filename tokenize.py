#!/usr/bin/python

"""
Module for tokenizing strings.
"""

def tokenorm(line):
  # Tokenize and normalize a string.
  punctuation = '!@#$%^&*()-_+=`~{}[]|\\\'";:/?<>,.\t'
  for p in punctuation:
    line = line.replace(p, ' ')
  return line.lower().split()

