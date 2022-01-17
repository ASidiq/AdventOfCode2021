
class AdventOfCodeDayOne():
    
    def __init__(self, depths):
        self.depths = depths.read()


    def find_increase(self):

        result = []
        measurements = self.depths.split("\n")
        measurements.remove("")

        for index, measurement in enumerate(measurements):
            if index == 0: pass

            if int(measurement) > int(measurements[index - 1]):
                result.append("increase")

        return(len(result))

    def find_increase_triplets(self):

        result = []
        measurements = self.depths.split("\n")
        measurements.remove("")
        measurements = [int(x) for x in measurements]

        for index, measurement in enumerate(measurements):
            try:
                a = [measurement, measurements[index+1], measurements[index+2]]
                b = [measurements[index+1], measurements[index+2],measurements[index+3]]
                if sum(b) > sum(a):
                    result.append("increase")
            except Exception as e:
                return(len(result))

    

if __name__== "__main__" :
    with open(file="./input.txt",mode='r') as input:

        problem = AdventOfCodeDayOne(input)

        solution_day_one = problem.find_increase()
        print(solution_day_one)

        solution_day_two = problem.find_increase_triplets()
        print(solution_day_two)
