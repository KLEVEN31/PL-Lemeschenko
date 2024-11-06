from math import prod
lst = [3, 4, 5, 6, 7, 4, 9, 8, 3, 9, 9, 3, 5] 
 
print(sum(lst[i] for i in range(1, len(lst), 2)))
print(prod(lst[j] for j in range(0, len(lst), 2)))
