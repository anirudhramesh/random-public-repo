import re

f = open('input4.txt')
inp_ = f.readlines()


def check_valid_1(new_ppt):
    if new_ppt.count(':') == 8 or (new_ppt.count(':') == 7 and 'cid:' not in new_ppt):
        return True
    return False


def check_valid_2(new_ppt):
    if new_ppt.count(':') < 7 or (new_ppt.count(':') == 7 and 'cid:' in new_ppt):
        return False

    try:
        byr = 1920 <= int(re.match(r'(?:.*byr:)(\d{4})\b', new_ppt).group(1)) <= 2002
        iyr = 2010 <= int(re.match(r'(?:.*iyr:)(\d{4})\b', new_ppt).group(1)) <= 2020
        eyr = 2020 <= int(re.match(r'(?:.*eyr:)(\d{4})\b', new_ppt).group(1)) <= 2030
        if (hgt := re.match(r'(?:.*hgt:)(\d+)cm', new_ppt)) is None:
            hgt = 59 <= int(re.match(r'(?:.*hgt:)(\d+)in', new_ppt).group(1)) <= 76
        else:
            hgt = 150 <= int(hgt.group(1)) <= 193
        re.match(r'(?:.*hcl:#)([0-9a-f]{6})\b', new_ppt).group(1)
        ecl = re.match(r'(?:.*ecl:)([a-z]{3})\b', new_ppt).group(1) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        re.match(r'(?:.*pid:)(\d{9})\b', new_ppt).group(1)
    except AttributeError:
        return False

    return byr & iyr & eyr & hgt & ecl


valid_passports = 0
new_ppt_details = ''
for line in inp_:
    if line == '\n':
        if check_valid_2(new_ppt_details[:-1]):
            valid_passports += 1
        new_ppt_details = ''
    new_ppt_details += line[:-1] + ' '
if check_valid_2(new_ppt_details[:-1]):
    valid_passports += 1

print(valid_passports)
