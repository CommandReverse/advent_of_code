import re

with open('day_4', 'r') as file:
    d = file.readlines()

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #'cid' is optional

def transform():
    list_of_dicts = []
    data = [i.strip("\n").strip("\n").replace(" ", ",").split(",") for i in d]
    data = [item for sublist in data for item in sublist]
    tmp = {}
    for item in data:
        if item:    
            k_v = item.split(":")
            tmp.update({k_v[0]: k_v[1]})
        else:
            list_of_dicts.append(tmp)
            tmp = {}
    return list_of_dicts

def split_up(s):
    p = re.compile('(\d+)\s*(\w+)')
    return p.match(s).groups()

if __name__ == "__main__":
    total = 0
    li = transform()
    for d in li:
        if len(set(FIELDS) & set(d.keys())) == len(FIELDS):
            tmp = split_up(d['hgt'])
            print(tmp[0])
            if not 1920 <= int(d['byr']) <= 2002:
                continue
            if not 2010 <= int(d['iyr']) <= 2020:
                continue
            if not 2020 <= int(d['eyr']) <= 2030:
                continue
            if tmp[1] == "cm" and 150 <= int(tmp[0]) >= 193:
                continue
            if tmp[1] == "in" and 59 <= int(tmp[0]) >= 76:
                continue
            if not re.match("^#[0-9a-f]{6}", d['hcl']):
                continue
            if not d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and not len(d['ecl']) == 1:
                continue
            if not d['pid'].isdigit() and not len(d['pid']) == 9:
                continue
            total += 1
    print(total)
    
