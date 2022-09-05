import re

f = open('input7.txt')
inp_ = f.read().split('\n')

bags = dict()
for line in inp_:
    matches = re.match(r'(.*) contain (.*)', re.sub(r'\s*bag(s*)\.*', '', line))
    holder = matches.group(1)
    held = dict()
    for match in matches.group(2).split(', '):
        if 'no other' in match:
            break
        split_match = re.match(r'^(\d+) (.*)', match)
        held.update({split_match.group(2): int(split_match.group(1))})
    bags.update({holder: held})


def find_target_bag(target_bag, all_bags, this_route, already_found=None):
    latest_bag = this_route[-1]

    if target_bag in all_bags[latest_bag].keys():
        already_found.extend(this_route)
        return None
    else:
        for bag in all_bags[latest_bag].keys():
            find_target_bag(target_bag, all_bags, this_route + [bag], already_found)


containers = []
target_ = 'shiny gold'
# for bag in bags.keys():
#     find_target_bag(target_, bags, [bag], containers)
# print(len(set(containers)))


def find_contained_bags(holding_bag, all_bags, contained_bags, multiplier):
    if len(all_bags[holding_bag]) == 0:
        return None
    else:
        for bag in all_bags[holding_bag].keys():
            val = all_bags[holding_bag][bag] * multiplier
            if bag in contained_bags.keys():
                contained_bags[bag] += val
            else:
                contained_bags[bag] = val
            find_contained_bags(bag, all_bags, contained_bags, val)


contained_ = {}
holding_bag_ = 'shiny gold'
find_contained_bags(holding_bag_, bags, contained_, 1)

print(sum(contained_.values()))
