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

def binary_diagnostic(data):

    gamma = []

    for i in range(0, len(data[0])):
        gamma.append(mostCommon(numAt(data, i)))

    epsilon = inverseBinary(gamma)

    return binaryToDecimal(gamma) * binaryToDecimal(epsilon)


if __name__ == "__main__":
    
    # Getting the input data
    data = lines(get_data(day=3, year=2021))
    
    # Part A: 3549854
    print(f"Answer: {binary_diagnostic(data)}")
