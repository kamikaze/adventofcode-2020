import re
from collections import deque
from itertools import combinations


def stream_data(f):
    """
    While it is possible to load all the numbers into RAM at once,
    I'm going to simulate real data stream from somewhere
    """
    yield from map(int, (line for line in f if line.strip()))


def part1() -> int:
    """
       I'm using limited deque to get built-in sliding window functionality. Instead of writing slow and verbose code.
    """
    preamble = deque(maxlen=25)

    with open('input09.txt') as f:
        data = stream_data(f)

        for _ in range(25):
            preamble.append(next(data))

        for number in stream_data(f):
            sums = set(map(sum, combinations(preamble, 2)))

            if number not in sums:
                print(f'Wrong number: {number}')

                return number

            preamble.append(number)
            

def part2(invalid_number: int):
    adds = deque()

    with open('input09.txt') as f:
        data = stream_data(f)

        for number in data:
            if number > invalid_number:
                adds.clear()

                continue

            adds.append(number)

            if len(adds) < 2:
                continue

            summed_number = sum(adds)

            while summed_number > invalid_number:
                left_number = adds.popleft()
                summed_number -= left_number

            if summed_number == invalid_number and len(adds) > 1:
                return min(adds) + max(adds)


if __name__ == '__main__':
    invalid_number = part1()
    encryption_weakness = part2(invalid_number)

    print(f'Encryption weakness: {encryption_weakness}')

