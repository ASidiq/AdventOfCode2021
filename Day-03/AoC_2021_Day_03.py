

class AdventOfCodeDayThree():

    def __init__(self, input):
        self.input = input.read()
        self.value_type = None
        self.column_to_read = 0
        #self.input = input

    def power_consumption(self):
        all_values = self.input.split("\n")
        all_values.remove("")
        binary_numbers = []
        for item in all_values:
            binary_numbers.append(list(item))
        columns_zipped = zip(*binary_numbers) #unpacking list items into zip function
        max_numbers = map(self.max_number, columns_zipped)
        gamma = list(max_numbers)
        epsilon = [str(int(x=='0')) for x in gamma]
        gamma_str = "".join(gamma)
        epsilon_str = "".join(epsilon)
        return int(gamma_str, 2) * int(epsilon_str, 2)

    def life_support_rating(self):
        all_values = self.input.split("\n")
        all_values.remove("")
        binary_numbers = []
        for item in all_values:
            binary_numbers.append(list(item))
        
        oxygen = self.o2_or_co2_value(binary_numbers, "most common")
        scrubber = self.o2_or_co2_value(binary_numbers, "least common")
        return int("".join(oxygen), 2) * int("".join(scrubber), 2)

    def o2_or_co2_value(self, binary_codes, value):
        self.value_type = value
        if len(binary_codes) == 1:
            self.column_to_read = 0
            return binary_codes[0]
        columns_zipped = zip(*binary_codes) #unpacking list items into zip function
        max_value_bin_codes =  map(self.max_and_least_number, [list(columns_zipped)[self.column_to_read]])
        self.column_to_read += 1
        return self.o2_or_co2_value([binary_codes[x] for x in list(max_value_bin_codes)[0]], value)   

    def max_number(self, tuple):
        print(tuple)
        zero = 0
        one = 0
        for number in tuple:
            if int(number) == 1:
                one += 1
            else:
                zero += 1
        
        if zero > one:
            return '0'

        return '1'

    def max_and_least_number(self, tuple):
        zero = 0
        one = 0
        zero_binary_code = []
        one_binary_code = []

        for index, number in enumerate(tuple):
            if int(number) == 1:
                one += 1
                one_binary_code.append(index)
            else:
                zero += 1
                zero_binary_code.append(index)
        
        if self.value_type == "most common":
            if zero > one:
                return zero_binary_code

            return one_binary_code
        
        if one < zero:
            return one_binary_code
        
        return zero_binary_code

    def power_consumption_test(self):
            all_values = self.input.split("\n")
            all_values.remove("")
            all_values.pop(-1)
            
            binary_numbers = []
            for item in all_values:
                binary_numbers.append(list(item.strip()))
            columns_zipped = zip(*binary_numbers)
            max_numbers = map(self.max_number, columns_zipped)
            gamma = list(max_numbers)
            epsilon = [str(int(x=='0')) for x in gamma]
            gamma_str = "".join(gamma)
            epsilon_str = "".join(epsilon)
            return int(gamma_str, 2) * int(epsilon_str, 2)
if __name__=="__main__":

    with open(file="./input.txt",mode='r') as input:

        sample = '''
                    00100
                    11110
                    10110
                    10111
                    10101
                    01111
                    00111
                    11100
                    10000
                    11001
                    00010
                    01010
                '''
        problem = AdventOfCodeDayThree(input)

        solution = problem.power_consumption()
        print(solution)

        life_support_solution = problem.life_support_rating()
        print(life_support_solution)
        