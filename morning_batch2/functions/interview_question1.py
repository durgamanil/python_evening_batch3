import itertools

x = [2,8,4,7,9,5,1]
target =10

for i in itertools.combinations(x,2):
    if sum(i) == target:
        print([x.index(j) for j in i])
