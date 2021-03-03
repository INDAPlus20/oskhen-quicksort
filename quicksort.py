#!/usr/bin/env python3
import math

def sort(lst):
    lst.sort()
    return lst

def quicksort(lst):

    def pivot(lst, lo, hi):
        mid = math.floor((lo+hi) / 2)
        if lst[mid] < lst[lo]:
            lst[lo], lst[mid] = lst[mid], lst[lo]
        if lst[hi] < lst[lo]:
            lst[lo], lst[hi] = lst[hi], lst[lo]
        if lst[mid] < lst[hi]:
            lst[mid], lst[hi] = lst[hi], lst[mid]
        
        return lst[hi]

    def partition(lst, lo, hi):

        pivot = lst[math.floor((lo+hi) / 2)]

        i = lo - 1
        j = hi + 1

        while True:
            i += 1
            while lst[i] < pivot:
                i += 1
    
            j -= 1
            while lst[j] > pivot:
                j -= 1

            if i >= j:
                return j

            lst[i], lst[j] = lst[j], lst[i]


    def internal(lst, lo, hi):
        if lo < hi:
            p = partition(lst, lo, hi)
            internal(lst, lo, p)
            internal(lst, p + 1, hi)
    
    internal(lst, 0, len(lst) - 1)

    return lst
    

if __name__ == '__main__':
    numbers = list(map(int, input().split(" ")[1:]))
    x = ' '.join(list(map(str, quicksort(numbers))))
    print(x)
    #print(f"{''.join(list(map(int, sort(numbers))))}")

