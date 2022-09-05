from collections import namedtuple
from typing import Tuple, Iterable, Dict, Union, List
from functools import reduce

import re
import operator

Number = Union[float, int]


def ints(text: str) -> Tuple[int]:
    "Return a tuple of all the integers in text."
    return mapt(int, re.findall('-?[0-9]+', text))


def mapt(fn, *args):
    "Do map(fn, *args) and make the result a tuple."
    return tuple(map(fn, *args))


def data(day: int, parser=str, sep='\n') -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    with open(f'input{day}.txt') as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))


def prod(numbers) -> Number:
    "The product of an iterable of numbers."
    return reduce(operator.mul, numbers, 1)


TicketData = namedtuple('TicketData', 'fields, your, nearby')

Ticket = ints  # A ticket is a tuple of ints


class Sets(tuple):
    "A tuple of set-like objects (such as ranges); supports `in`."

    def __contains__(self, item): return any(item in s for s in self)


def parse_ticket_sections(fieldstr: str, your: str, nearby: str) -> TicketData:
    return TicketData(fields=dict(map(parse_ticket_line, fieldstr)),
                      your=Ticket(your[1]),
                      nearby=[Ticket(line) for line in nearby[1:]])


def parse_ticket_line(line: str) -> Tuple[str, Sets]:
    "Parse 'row: 10-20 or 30-40' to ('row', Sets((range(10, 21), range(30, 41))))."
    field = line.split(':')[0]
    a, b, c, d = ints(line.replace('-', ' '))
    return field, Sets((range(a, b + 1), range(c, d + 1)))


def lines(text: str) -> List[str]:
    "Split the text into a list of lines."
    return text.strip().splitlines()


in16 = parse_ticket_sections(*data(16, lines, sep='\n\n'))


def valid_ticket(ticket, ranges) -> bool: return all(v in ranges for v in ticket)


def decode_tickets(ticket_data) -> Dict[str, int]:
    "Return a mapping of {field_name: field_number} (index into ticket)."
    fields, your, nearby = ticket_data
    ranges = Sets(ticket_data.fields.values())
    valid = [t for t in nearby + [your] if valid_ticket(t, ranges)]
    possible = {i: set(fields) for i in range(len(your))}
    while any(len(possible[i]) > 1 for i in possible):
        for field_name, i in invalid_fields(valid, fields):
            possible[i] -= {field_name}
            if len(possible[i]) == 1:
                eliminate_others(possible, i)
    return {field: i for i, [field] in possible.items()}


def invalid_fields(valid, fields) -> Iterable[Tuple[str, int]]:
    "Yield (field_name, field_number) for all invalid fields."
    return ((field_name, i) for ticket in valid for i in range(len(ticket))
            for field_name in fields
            if ticket[i] not in fields[field_name])


def eliminate_others(possible, i):
    "Eliminate possible[i] from all other possible[j]."
    for j in possible:
        if j != i:
            possible[j] -= possible[i]


def day16_2(ticket_data):
    "The product of the 6 fields that start with 'departure'."
    code = decode_tickets(ticket_data)
    return prod(ticket_data.your[code[field]]
                for field in code if field.startswith('departure'))


print(day16_2(in16))
