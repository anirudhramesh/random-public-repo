from operator import mul, add
from functools import reduce
import re

f = open('input18.txt')
inp_ = f.read().split('\n')

# part 1
def eval_expr_part1(expr):
    accum = None
    oper = None
    oper_mapping = {'+': add, '*': mul}
    digits = [str(i) for i in range(10)]
    expr = expr.replace(' ', '')
    char_num = 0
    while char_num < len(expr):
        if expr[char_num] in digits:
            number = int(re.match(r'[\d]\b', expr[char_num:])[0])
            if accum is None:
                accum = number
            else:
                accum = oper(accum, number)
            char_num += len(str(number))
        elif expr[char_num] in oper_mapping:
            oper = oper_mapping[expr[char_num]]
            char_num += 1
        elif expr[char_num] == '(':
            open_, start_ = 1, char_num+1
            while open_ > 0:
                char_num += 1
                if expr[char_num] == '(':
                    open_ += 1
                elif expr[char_num] == ')':
                    open_ -= 1
            number = eval_expr_part1(expr[start_:char_num])
            if accum is None:
                accum = number
            else:
                accum = oper(accum, number)
            char_num += 1
    return accum


# print(sum([eval_expr_part1(line) for line in inp_]))



# part 2
# def do_operation(accum, oper, number):
#     if accum is None:
#         accum = number
#     elif oper == add:
#         accum = oper(accum, number)
#     else:
#         mul_expr = str(accum) + '*'
#         accum = number


def eval_expr_part2(expr):
    accum = None
    oper = None
    oper_mapping = {'+': add, '*': mul}
    digits = [str(i) for i in range(10)]
    expr = expr.replace(' ', '')
    char_num = 0
    mul_list = []
    while char_num < len(expr):
        if expr[char_num] in digits:
            number = int(re.match(r'[\d]\b', expr[char_num:])[0])
            if accum is None:
                accum = number
            elif oper == add:
                accum = oper(accum, number)
            else:
                # mul_expr += str(accum) + ' * '
                mul_list.append(accum)
                accum = number
            char_num += len(str(number))
        elif expr[char_num] in oper_mapping:
            oper = oper_mapping[expr[char_num]]
            char_num += 1
        elif expr[char_num] == '(':
            open_, start_ = 1, char_num+1
            while open_ > 0:
                char_num += 1
                if expr[char_num] == '(':
                    open_ += 1
                elif expr[char_num] == ')':
                    open_ -= 1
            number = eval_expr_part2(expr[start_:char_num])
            if accum is None:
                accum = number
            elif oper == add:
                accum = oper(accum, number)
            else:
                # mul_expr += str(accum) + '*'
                mul_list.append(accum)
                accum = number
            char_num += 1
    mul_list.append(accum)
    return reduce(mul, mul_list)


print(sum([eval_expr_part2(line) for line in inp_]))
