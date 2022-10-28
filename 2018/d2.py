#AOC 2018 day 2

from collections import Counter

with open('./2018/day2/input.txt') as f:
    lines = f.readlines()

    #print(f"{lines}")
    lines = [l.strip() for l in lines]
    #print(f"{lines}")
        
    def part1():
        

        #use counter.Values() to get values
        two = 0
        two_1 = 0
        three = 0
        for line in lines:
        
            c = Counter(line).values()

            print(c)

            #op 1
            two += 2 in c
            three += 3 in c

        print(two*three)

    def part2():

        for l1 in lines:
            for l2 in lines:
                s = ''.join(x for x, y in zip(l1,l2) if x == y)
                
                if len(s) == len(l1)-1:
                    return s

print(part1())
print(part2())