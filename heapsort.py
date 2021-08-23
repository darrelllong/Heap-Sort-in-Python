#!/usr/bin/env python3

# Adapted from Sara Baase's "Computer Algorithms"

def maxChild(seq, first, last):
    left  = 2 * first
    right = left + 1;
    return right if right < last and seq[right] > seq[left] else left

def fixHeap(seq, first, last):
    found  = False
    father = first
    great  = maxChild(seq, father, last)
    root   = seq[first]
    while father <= last // 2 and not found:
        if root < seq[great]:
             seq[father] = seq[great]
             father = great
             great = maxChild(seq, father, last)
        else:
             found = True
    seq[father] = root

def buildHeap(seq, last):
    for father in range(last // 2, -1, -1):
        fixHeap(seq, father, last)

def heapSort(seq):
    first = 0
    last  = len(seq)
    buildHeap(seq, last)
    for leaf in range(last - 1, -1, -1):
        seq[first], seq[leaf] = seq[leaf], seq[first],
        fixHeap(seq, first, leaf - 1)

from random import randrange as uniform

x = [ uniform(50) for _ in range(1, 20) ]

print(x)
heapSort(x)
print(x)
