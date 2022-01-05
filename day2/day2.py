def main():
    # forward x => horizontal += x and depth += aim * x
    # down x => aim += x
    # up x => aim -= x

    path = 'day2.txt'
    file = open(path, 'r')

    horizontal = 0
    depth = 0
    aim= 0

    for line in file:
        splited = line.split()
        if splited[0] == 'down':
            aim += int(splited[1])
        if splited[0] == 'up':
            aim -= int(splited[1])
        if splited[0] == 'forward':
            depth += int(splited[1]) * aim
            horizontal += int(splited[1])

    mutliply_result = depth * horizontal
    print(mutliply_result)

    file.close()
