f = open('input3.txt')
inp_ = f.read().split('\n')

# the input parsing is so messed up in windows but this guy's code works perfectly somehow
# def data(day: int, parser=str, sep='\n') -> list:
#     "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
#     with open(f'input{day}.txt') as f:
#         sections = f.read().rstrip().split(sep)
#         return list(map(parser, sections))
#
#
# norvig_input = data(3)


def traverse(slope, inp_copy=inp_):
    width = len(inp_copy[0])
    trees_hit = 0
    start = [0, 0]
    while start[0] < len(inp_copy):
        if inp_copy[start[0]][start[1]] == '#':
            trees_hit += 1
        start[0] += slope[0]
        start[1] += slope[1]

        if start[1] >= width:
            start[1] %= width

    return trees_hit


# part_1 = traverse((1, 3))
# print(part_1)

part_2 = traverse((1, 1)) * traverse((1, 3)) * traverse((1, 5)) * traverse((1, 7)) * traverse((2, 1))
print(part_2)
