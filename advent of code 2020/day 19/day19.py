from itertools import product
import re

def read_input(input_file):
    f = open(input_file)
    rules_text, messages = f.read().split('\n\n')

    rules_text = rules_text.split('\n')
    messages = messages.split('\n')

    rules = {}
    for rule in rules_text:
        rule_num, contents = rule.split(': ')
        rules.update({int(rule_num): contents})

    return rules, messages


def parse_rules(all_rules, deciphered_rules, rule_num):
    if rule_num in deciphered_rules:
        return deciphered_rules[rule_num]
    content = all_rules[rule_num]
    if '"' in content:
        this_rule = content.replace('"', '')
    else:
        rule_combinations = content.split(' | ')
        this_rule = []
        for comb in rule_combinations:
            combination_rule = product(*[parse_rules(all_rules, deciphered_rules, int(rule_num_1)) for rule_num_1 in comb.split(' ')])
            # this_rule += [''.join(combo) for combo in combination_rule]
            this_rule.append(combination_rule)
    deciphered_rules.update({rule_num: this_rule})
    return this_rule


# part 1
def do_part1(rules, messages):
    rule_zero = parse_rules(rules, dict(), 0)

    matches = 0
    for msg in messages:
        if msg in rule_zero:
            matches += 1

    print(matches)


# part 2
def part_2(rules, messages):
    inf_loop_rules = ['8: 42 | 42 8', '11: 42 31 | 42 11 31']
    some_constant = 5000

    for rule in inf_loop_rules:
        rule_num, contents = rule.split(': ')
        rule_num = int(rule_num)
        if rule_num in rules:
            rules.update({rule_num*some_constant: rules[rule_num],
                          rule_num: re.sub(r'\b'+str(rule_num)+r'\b', str(rule_num*some_constant), contents)})

    do_part1(rules, messages)


rules, messages = read_input('input19.txt')
# do_part1(rules, messages)  # 107
part_2(rules, messages)
