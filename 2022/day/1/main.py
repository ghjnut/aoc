#!/usr/bin/env python3

FILE = "day/1/input"


def main():
    elves = init()
    biggest_elf = get_biggest_elf(elves)
    elves_rsorted = get_rsorted(elves)
    top_3 = elves_rsorted[0:3]

    print(biggest_elf.total_calories)
    print(sum(x.total_calories for x in top_3))


def init():
    elves = []
    with open(FILE) as data:
        line = data.readline()
        foods = []
        while line:
            if line == "\n":
                if len(foods) > 0:
                    elf = Elf(foods)
                    elves.append(elf)
                    foods = []
            else:
                foods.append(int(line.strip()))
            line = data.readline()

    return elves


def get_biggest_elf(elves):
    biggest_elf = None
    for elf in elves:
        if biggest_elf == None or elf.total_calories > biggest_elf.total_calories:
            biggest_elf = elf

    return biggest_elf


def get_rsorted(elves):
    elves.sort(key=lambda x: x.total_calories, reverse=True)
    return elves


class Elf:
    def __init__(self, food):
        self.food = food

    @property
    def total_calories(self):
        return sum(self.food)


if __name__ == "__main__":
    main()
