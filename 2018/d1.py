#AOC 2018 Day 1

with open('./2018/day1/input.txt') as f:
    lines = f.readlines()

    print(f"{lines}")

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    def part1():

            s = sum(map(int, lines))
            print(f"contents: {lines}")
            print(f"final value: {s}")

    def part2():
            s = 0
            seen = set([s])

            while True:
                for line in lines:
                    s += int(line)
                    
                    if s in seen:
                        return s
                    
                    seen.add(s)

            print(f"final value: {s}")


    
print(part1())
print(part2())