#!/usr/bin/env python3
import math

INSERT_SWITCH = 10 # Empirically tested

def sort(lst):

    def insert_sort(lst, lo, hi):
        for i in range(lo, hi):
            for j in range(i, 0, -1):
                if lst[j] < lst[j-1]:
                    lst[j], lst[j-1] = lst[j-1], lst[j]
                else:
                    break

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


    def quicksort(lst, lo, hi):
        if lo < hi:
            if hi - lo < INSERT_SWITCH:
                insert_sort(lst, lo, hi+1)
            else:
                p = partition(lst, lo, hi)
                quicksort(lst, lo, p)
                quicksort(lst, p + 1, hi)
    

    quicksort(lst, 0, len(lst) - 1)

    return lst
    


if __name__ == '__main__':
    numbers = list(map(int, input().split(" ")[1:]))
    x = ' '.join(list(map(str, sort(numbers))))
    print(x)
    #print(f"{''.join(list(map(int, sort(numbers))))}")

