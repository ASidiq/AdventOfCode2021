from __future__ import division
import numpy as np


class AdventOfCodeDayFive():

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.vertical_lines = []
        self.horizontal_lines = []
        self.diagonal_lines = []
        self.all_coordinates = []
        self.map_points_counts = {}
        pass

    def solution(self):
        self.find_horizontal_vertical_lines()
        self.find_inbetween_points()
        return self.find_crossovers()

    def solution_v2(self):
        self.find_horizontal_vertical_lines()
        self.find_inbetween_points_v2()
        return self.find_crossovers()

    def find_horizontal_vertical_lines(self):
        for line in self.coordinates:
            if int(line[0][0]) == int(line[1][0]):
                self.vertical_lines.append(self.zip_line_coordinates(line))
            elif int(line[0][1]) == int(line[1][1]):
                self.horizontal_lines.append(self.zip_line_coordinates(line))
            else:
                self.diagonal_lines.append(self.zip_line_coordinates(line))



    def zip_line_coordinates(self, line):
        return ([int(line[0][0]),int(line[1][0])], \
                [int(line[0][1]),int(line[1][1])])
    
    def find_inbetween_points(self):
        points = []
        for point in self.vertical_lines:
            self.all_coordinates += [(point[0][0], x) for x in range(min(point[1]), max(point[1])+1)]
        
        for point in self.horizontal_lines:
            self.all_coordinates += [(x,point[1][0]) for x in range(min(point[0]), max(point[0])+1)]

          
    def find_inbetween_points_v2(self):
        
        for point in self.vertical_lines:
            self.all_coordinates += [(point[0][0], x) for x in range(min(point[1]), max(point[1])+1)]
        
        for point in self.horizontal_lines:
            self.all_coordinates += [(x,point[1][0]) for x in range(min(point[0]), max(point[0])+1)]

        for line in self.diagonal_lines:
            gradient = self.find_gradient(line)
            y_intercept = self.find_y_intercept(line, gradient)
            self.all_coordinates += [(x, int(gradient*x + y_intercept)) for x in range(min(line[0]), max(line[0])+1)]
        
    def find_gradient(self, point):
        gradient = int((point[1][1] - point[1][0]) / (point[0][1] - point[0][0]))
        return gradient

    def find_y_intercept(self, line, gradient):
        intercept = line[1][0] - (gradient * line[0][0])
        return intercept

    def find_crossovers(self):
        count = 0
        for single_point in self.all_coordinates:
            if single_point in self.map_points_counts:
                self.map_points_counts[single_point] += 1
            else:
                self.map_points_counts[single_point] = 1
        return len([x for x in self.map_points_counts.values() if x >= 2])
        
          

 
if __name__== "__main__":


    with open(file="./Coordinates.txt",mode='r') as numbers_input:
        numbers = numbers_input.read()
        points = [x.split("->") for x in numbers.split("\n") ]
        points = [(i[0].strip().split(","), i[1].strip().split(",")) for i in points]
        problem = AdventOfCodeDayFive(points)
        
        # only run one of the solutions at any point in time as the two solutions share variables 
        result = problem.solution()
        print(result)

        result2 = problem.solution_v2()
        print(result2)