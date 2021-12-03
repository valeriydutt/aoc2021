from aocd import get_data
from aocd.transforms import lines

def numAt(data, index):

    binaryArray = []

    for i in range(0, len(data)):
        binaryArray.append(data[i][index])

    return binaryArray

def mostCommon(array):

    ones = 0
    zeros = 0

    for char in array:
        if(int(char) == 1):
            ones += 1
        else:
            zeros += 1
    
    if(ones > zeros):
        return 1
    else:
        return 0

def inverseBinary(array):

    inverse = []

    for char in array:
        if(int(char) == 1):
            inverse.append(0)
        else:
            inverse.append(1)

    return inverse

def binaryToDecimal(array):

    decimal = 0

    for char in array:
        decimal = decimal*2 + int(char)
    
    return decimal

def power_consumption(data):

    gamma = []

    for i in range(0, len(data[0])):
        gamma.append(mostCommon(numAt(data, i)))

    epsilon = inverseBinary(gamma)
    print(epsilon)
    return binaryToDecimal(gamma) * binaryToDecimal(epsilon)

def oxygen_rating(data):

    oxygen = data

    for i in range(len(data[0])):

        while(len(oxygen) > 1):
            
            num = mostCommon(numAt(data, i))

            for j in range(len(data)):

                if(int(data[j][i]) != num):
                    oxygen.remove(data[j])

    return binaryToDecimal(oxygen)

def co2_rating(data):
    return 0

def life_support_rating(data):
    return oxygen_rating(data)

if __name__ == "__main__":
    
    # Getting the input data
    data = lines(get_data(day=3, year=2021))
    # Part A: 3549854
    print(f"Part A Answer: {power_consumption(data)}")
    # Part A:
    print(f"Part B Answer: {life_support_rating(data)}")
