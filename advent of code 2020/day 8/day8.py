f = open('input8.txt')
commands = f.read().split('\n')

inst_executed = []
accumulator = [0]
inst_number = 0
while inst_number not in inst_executed:
    op, arg = commands[inst_number].split(' ')
    inst_executed.append(inst_number)

    if op == 'nop':
        inst_number += 1
        accumulator.append(accumulator[-1])
    elif op == 'acc':
        accumulator.append(accumulator[-1] + int(arg))
        inst_number += 1
    elif op == 'jmp':
        inst_number += int(arg)
        accumulator.append(accumulator[-1])

# part 1
# print(accumulator[-1])

inst_executed_copy = inst_executed.copy()
accumulator_copy = accumulator.copy()
last_edited_inst = len(inst_executed_copy)
while inst_number < len(commands):
    if inst_number in inst_executed_copy:
        commands_copy = commands.copy()
        for inst_ in range(last_edited_inst-1, -1, -1):
            op, arg = commands[inst_executed[inst_]].split(' ')
            if op == 'jmp' or op == 'nop':
                last_edited_inst = inst_
                break

        if op == 'jmp':
            commands_copy[inst_executed[last_edited_inst]] = ' '.join(['nop', arg])
        elif op == 'nop':
            commands_copy[inst_executed[last_edited_inst]] = ' '.join(['jmp', arg])

        inst_executed_copy = inst_executed_copy[:last_edited_inst]
        accumulator_copy = accumulator_copy[:last_edited_inst]
        inst_number = inst_executed_copy[-1]

    op, arg = commands_copy[inst_number].split(' ')
    inst_executed_copy.append(inst_number)

    if op == 'nop':
        inst_number += 1
        accumulator_copy.append(accumulator_copy[-1])
    elif op == 'acc':
        accumulator_copy.append(accumulator_copy[-1] + int(arg))
        inst_number += 1
    elif op == 'jmp':
        inst_number += int(arg)
        accumulator_copy.append(accumulator_copy[-1])

# part 2
print(accumulator_copy[-1])
