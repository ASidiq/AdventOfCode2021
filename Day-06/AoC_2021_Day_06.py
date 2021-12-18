from __future__ import division
import numpy as np


class AdventOfCodeDaySix():

    def __init__(self, fish):
        self.fish = fish
        self.life_and_fish = dict()
        self.fish_got_days_left = None
        
        
    def main(self):
        self.map_fish_to_life()

        for days in range(0, 256):
            self.remove_a_life()

        return sum([x for x in self.life_and_fish.values()])

    def map_fish_to_life(self):
        for life in range (0, 9):
            self.life_and_fish[life] = 0
        
        for fish in self.fish:
            self.life_and_fish[fish] += 1

    def remove_a_life(self):
        count_of_fish_at_zero = self.life_and_fish[0]
        for life in range(0, 8):
            self.life_and_fish[life] = self.life_and_fish[life+1] if life != 6 \
            else self.life_and_fish[life+1] + count_of_fish_at_zero

        self.life_and_fish[8] = count_of_fish_at_zero

    
 
if "__main__"==__name__:

    #numbers = None
    with open(file="./input.txt",mode='r') as numbers_input:
        numbers = numbers_input.read()
        fish = [int(x) for x in numbers.split(",") ]
        problem = AdventOfCodeDaySix(fish)
        solution = problem.main()
        print(solution)

