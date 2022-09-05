def part1(target, starting_input):
    for _ in range(target-len(starting_input)):
        try:
            find = starting_input[-2::-1].index(starting_input[-1])
            starting_input.append(find+1)
        except ValueError:
            starting_input.append(0)
    return starting_input[-1]


starting_input = [8, 0, 17, 4, 1, 12]
target = 2020

# print(part1(target, starting_input))


def part2(target, starting_input):
    index_ = {val: starting_input.index(val) for val in starting_input[:-1]}
    length = len(starting_input)
    last_val = starting_input[-1]
    while length < target:
        found = index_.get(last_val, None)
        index_.update({last_val: length-1})
        if found is None:
            next_val = 0
        else:
            next_val = length - found - 1
        last_val = next_val
        length += 1
    return last_val



target = 30_000_000
starting_input = [8, 0, 17, 4, 1, 12]

print(part2(target, starting_input))
