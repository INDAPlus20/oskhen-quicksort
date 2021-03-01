#!/usr/bin/env python3

def sort(lst):
    lst.sort()
    return lst

def quicksort(lst):

    def partition(lst, lo, hi):
        pivot = lst[hi]
        i = lo
        for j in range(lo, hi+1):
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i = i+1
        lst[i], lst[hi] = lst[hi], lst[i]
        return i

    def internal(lst, lo, hi):
        if lo < hi:
            p = partition(lst, lo, hi)
            internal(lst, lo, p-1)
            internal(lst, p + 1, hi)
    
    internal(lst, 0, len(lst) - 1)

    return lst
    

if __name__ == '__main__':
    numbers = list(map(int, input().split(" ")[1:]))
    x = ' '.join(list(map(str, quicksort(numbers))))
    print()
    #print(f"{''.join(list(map(int, sort(numbers))))}")

