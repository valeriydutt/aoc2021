from aocd import get_data
from aocd.transforms import lines

def dive(data):

    aim = 0
    horizontalPos = 0
    depthPos = 0

    for i in range(0, len(data)):

        chunk = data[i].split()
        firstLetter = chunk[0][0]
        distance = int(chunk[1])

        if(firstLetter == 'f'):
            horizontalPos += distance
            depthPos += (aim * distance)
        elif(firstLetter == 'd'):
            aim += distance
        elif(firstLetter == 'u'):
            aim -= distance
        

    return horizontalPos * depthPos

if __name__ == "__main__":
    
    # Getting the input data
    data = lines(get_data(day=2, year=2021))

    # Part A: 1692075; Part B: 1749524700
    print(f"Answer: {dive(data)}")
