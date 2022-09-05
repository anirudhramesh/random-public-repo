import numpy as np

f = open('input9.txt')
inp_ = np.array([int(x) for x in f.read().split('\n')])

# part 1

preamble_length = 25
for i in range(preamble_length, len(inp_)):
    prev_amble = inp_[i-preamble_length:i]
    diffs = inp_[i] - prev_amble
    if not any(x in prev_amble for x in diffs):
        break

print(inp_[i])

# part 2

new_target = inp_[i]

# new_target = 127
# inp_ = [35, 20, 15, 25, 47, 40, 62, 55, 65]
length = 1
lowest_index = 0
total = 0
while total != new_target and lowest_index + length <= len(inp_):
    length += 1
    total = np.sum(inp_[lowest_index:lowest_index+length])
    while total > new_target and length > 1:
        lowest_index += 1
        length -= 1
        total = np.sum(inp_[lowest_index:lowest_index+length])


print(min(inp_[lowest_index:lowest_index+length]) + max(inp_[lowest_index:lowest_index+length]))
