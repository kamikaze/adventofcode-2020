from collections import defaultdict


def part1():
    def count_bags(bag: str, rules: dict, touched: set) -> int:
        """
           The "touched" set is being used to track nodes which were already visited.
           In this part I'm building an inverse graph so I can go straight from
           "shiny gold" bag to its "parents".
        """
        if bag in touched:
            return 0

        touched.add(bag)
        cnt = 1

        try:
            for outer_bag in rules[bag]:
                cnt += count_bags(outer_bag, rules, touched)
        except KeyError:
            pass

        return cnt

    with open('input07.txt') as f:
        rules = defaultdict(dict)

        for line in filter(None, f):
            line = line.replace('bags', 'bag')
            outer_bag, inner_bags = line.split(' bag contain ')
            inner_bags = inner_bags[:-2].split(', ')
            
            for inner_bag in inner_bags:
                cnt, inner_bag = inner_bag[:-4].split(' ', maxsplit=1)

                try:
                    rules[inner_bag][outer_bag] = int(cnt)
                except ValueError:
                    rules[inner_bag][outer_bag] = 0

        rules = dict(rules)
        touched = set()
        cnt = count_bags('shiny gold', rules, touched) - 1

        print(f'Count: {cnt}')


def part2():
    def count_bags(bag: str, rules: dict) -> int:
        cnt = 0

        try:
            for inner_bag, inner_cnt in rules[bag].items():
                cnt += inner_cnt * count_bags(inner_bag, rules)
        except KeyError:
            pass

        return cnt + 1

    with open('input07.txt') as f:
        rules = defaultdict(dict)

        for line in filter(None, f):
            line = line.replace('bags', 'bag')
            outer_bag, inner_bags = line.split(' bag contain ')
            inner_bags = inner_bags[:-2].split(', ')

            for inner_bag in inner_bags:
                cnt, inner_bag = inner_bag[:-4].split(' ', maxsplit=1)

                try:
                    rules[outer_bag][inner_bag] = int(cnt)
                except ValueError:
                    rules[outer_bag][inner_bag] = 0

        rules = dict(rules)
        cnt = count_bags('shiny gold', rules) - 1

        print(f'Count: {cnt}')


if __name__ == '__main__':
    part1()
    part2()

