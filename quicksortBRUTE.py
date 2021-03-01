import quicksort
import random

i = 0
while True:
    print(i)
    lst = [random.randint(0, 1_000_000) for _ in range(random.randint(1, 500_000))]
    quicksort.quicksort(lst)
    i += 1
