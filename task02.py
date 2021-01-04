import re
from collections import Counter


def part1():
    with open('input02.txt') as f:
        pattern = re.compile(r'(\d+)-(\d+) ([a-zA-Z]): (.+)')
        cnt = 0

        for line in f:
            if match := pattern.match(line):
                count = Counter(match.group(4))

                if int(match.group(1)) <= count[match.group(3)] <= int(match.group(2)):
                    cnt += 1

        print(f'Valid password count: {cnt}')


def part2():
    with open('input02.txt') as f:
        pattern = re.compile(r'(\d+)-(\d+) ([a-zA-Z]): (.+)')
        cnt = 0

        for line in f:
            if match := pattern.match(line):
                password = match.group(4)
                count = Counter((password[int(match.group(1))-1], password[int(match.group(2))-1]))
                char = match.group(3)
                
                if count[char] == 1:
                    cnt += 1

        print(f'Valid password count: {cnt}')
    

if __name__ == '__main__':
    part1()
    part2()

