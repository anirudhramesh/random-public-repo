from functools import reduce
from operator import and_

f = open('input.txt')
inp_ = f.read().rstrip().split('\n\n')

# part 1
sum_ = 0
for line in inp_:
    sum_ += len(set(line.replace('\n', '')))

# print(sum_)


# part 2
sum_ = 0
for line in inp_:
    sets = [set(l) for l in line.split('\n')]
    sum_ += len(reduce(and_, sets))

print(sum_)
