from itertools import permutations

comb = permutations([-1,2-1,2,3,4,5,6,7],3)

print(len(list(comb)))
number = 5
for i in comb:
    if(sum(list(i))==5):
        print(i)