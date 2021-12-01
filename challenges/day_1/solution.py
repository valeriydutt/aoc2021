from aocd import get_data
from aocd.transforms import numbers

"""
Part A & B

Combined the solutions into 1 method with parametarized options to solve both problems
"""
def count_depth_increment(data, window_size=1):

    # Offsets the count from the first index
    count = -1
    prevSum = 0

    for i in range (len(data) - window_size + 1):

        currSum = sum(data[i: i + window_size])

        if (currSum > prevSum):
            count += 1

        prevSum = currSum

    return count

if __name__ == "__main__":
    
    # Getting the input data
    data = numbers(get_data())

    # 1400
    print(f"Part A answer: {count_depth_increment(data)}")
    # 1429
    print(f"Part B answer: {count_depth_increment(data, 3)}")