# AOC Day 3
import re
from collections import defaultdict


with open('./2018/day3/input.txt') as f:

    lines = f.readlines()

    d = defaultdict(set)
    for line in lines:
        #unpack the each number per line
        id, x, y, w, h = map(int, re.findall(r'\d+',line))

        for row in range(y, y+h):
            for col in range(x, x+w):
                d[(col,row)].add(id)
        
    print(sum(len(z) > 1 for z in d.values()))
        #(x,y) add id as a value

    correct_ids, invalid_ids = set(),set()

    for x in d.values():
        correct_ids |= x
        if len(x) > 1:
            invalid_ids |= x
    
    print(correct_ids - invalid_ids)