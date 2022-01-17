class AdventOfCodeDayTwo():

    def __init__(self, input):
        self.input = input.read()

    def find_location(self):
        instructions = self.input.split("\n")
        instructions.remove("")
        horizontal = 0
        depth = 0
        for rule in instructions:
            move = rule.split(" ")
            direction = move[0]
            value = int(move[1])

            if direction == "up":
                depth -= value
            elif direction == "down":
                depth += value
            elif direction == "forward":
                horizontal += value

        return depth * horizontal
    
    def find_location_revised(self):
        instructions = self.input.split("\n")
        instructions.remove("")
        horizontal = 0
        depth = 0
        aim = 0
        for rule in instructions:
            move = rule.split(" ")
            direction = move[0]
            value = int(move[1])

            if direction == "up":
                aim -= value
            elif direction == "down":
                aim += value
            elif direction == "forward":
                horizontal += value
                depth += aim*value
        return depth * horizontal
if __name__=="__main__":

    with open(file="./input.txt",mode='r') as input:

        problem = AdventOfCodeDayTwo(input)

        #solution = problem.find_location()
        #print(solution)

        revised_solution = problem.find_location_revised()
        print(revised_solution)