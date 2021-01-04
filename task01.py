import math
from itertools import combinations


def find_2020_numbers(values, cnt=2):
    for combo in combinations(values, cnt):
        if sum(combo) == 2020:
            print(f'{combo}, {math.prod(combo)}')

            return


def main():
    with open('input01.txt') as f:
        values = tuple(map(int, (line for line in f if line.strip())))
    
    find_2020_numbers(values, 2)
    find_2020_numbers(values, 3)


if __name__ == '__main__':
    main()

