from itertools import chain
import numpy as np
from functools import reduce
from operator import mul

f = open('input16.txt')

text_rules, your_ticket, nearby_tickets = f.read().split('\n\n')

your_ticket = [int(x) for x in your_ticket.split('\n')[1].split(',')]
nearby_tickets = [[int(x) for x in line.split(',')] for line in nearby_tickets.split('\n')[1:]]

rules_ = {}
for line in text_rules.split('\n'):
    rule, limits = line.split(': ')
    left, right = limits.split(' or ')
    left_low, left_high = (int(x) for x in left.split('-'))
    right_low, right_high = (int(x) for x in right.split('-'))
    rules_.update({rule: list(chain(range(left_low, left_high+1), range(right_low, right_high+1)))})

# part 1

all_valid_values = set(list(chain(*rules_.values())))
# print(sum([num for ticket in nearby_tickets for num in ticket if num not in all_valid_values]))


# part 2 - took forever to complete because I missed that both ends of the ranges were inclusive so the rule fitting
# was not one-to-one

valid_nearby_tickets = [ticket for ticket in (nearby_tickets + [your_ticket]) if all(nums in all_valid_values for nums in ticket)]

field_ranges_nearby_tickets = [set(x) for x in np.array(valid_nearby_tickets).T]
field_range_rules = [set(x) for x in rules_.values()]

field_rules_matches = [set(np.where([ticket_field <= rule_range for rule_range in field_range_rules])[0]) for ticket_field
                       in field_ranges_nearby_tickets]

field_rule_final_match = {}
while len(field_rule_final_match) < len(rules_):
    for field_num in range(len(field_rules_matches)):
        if len(field_rules_matches[field_num]) > 1:
            eliminate_rest = field_rules_matches[field_num] - set(chain.from_iterable(field_rules_matches[:field_num] +
                                                                                      field_rules_matches[field_num+1:]))
        else:
            eliminate_rest = field_rules_matches[field_num]

        if len(eliminate_rest) == 1:
            field_rule_final_match.update({list(eliminate_rest)[0]: field_num})
            field_rules_matches = [(rule - eliminate_rest) for rule in field_rules_matches]
            field_rules_matches[field_num] = set()

rule_names = list(rules_.keys())
departure_rules = [rule_num for rule_num in range(len(rule_names)) if rule_names[rule_num].startswith('departure')]

print(reduce(mul, [your_ticket[field_rule_final_match[i]] for i in departure_rules], 1))
