#!/usr/bin/env python3

# Adapted from Sara Baase's "Computer Algorithms"

def maxChild(seq, first, last):
    left  = 2 * first
    right = left + 1
    return right if right <= last and seq[right] > seq[left] else left

def fixHeap(seq, first, last):
    found  = False
    father = first
    great  = maxChild(seq, father, last)
    while father <= last // 2 and not found:
        if seq[father] < seq[great]:
            seq[father], seq[great] = seq[great], seq[father]
            father = great
            great = maxChild(seq, father, last)
        else:
            found = True

def buildHeap(seq, last):
    for father in range(last // 2, -1, -1):
        fixHeap(seq, father, last)

def heapSort(seq):
    first = 0
    last  = len(seq) - 1
    buildHeap(seq, last)
    for leaf in range(last, first, -1):
        seq[first], seq[leaf] = seq[leaf], seq[first],
        fixHeap(seq, first, leaf - 1)

def is_sorted(seq):
    for i in range(1, len(seq)):
        if seq[i - 1] > seq[i]:
            return False
    return True

from random import randrange as uniform

def main():
    x = [ uniform(10000) for _ in range(1, 10000) ]

    print(x[1:20])
    heapSort(x)
    assert(is_sorted(x))
    print(x[1:20])

if __name__ == '__main__': main()
