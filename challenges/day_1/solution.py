from aocd import get, get_data
from aocd.transforms import numbers

"""
Part A
"""
def count_depth_increment(data):
    count = 0

    for i in range (0, len(data) - 1):
        if (data[i] < data[i + 1]):
            count += 1

    return count

"""
Part B
"""


if __name__ == "__main__":
    
    # Getting the input data
    data = numbers(get_data())

    print(f"Part A answer: {count_depth_increment(data)}")