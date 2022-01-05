def main():
    # forward x => horizontal += x
    # down x => depth += x
    # up x => deph -= x

    path = 'day2.txt'
    file = open(path, 'r')

    horizontal = 0
    depth = 0

    for line in file:
        splited = line.split()
        if splited[0] == 'forward':
            horizontal += int(splited[1])
        if splited[0] == 'up':
            depth -= int(splited[1])
        if splited[0] == 'down':
            depth += int(splited[1])

    mutliply_result = depth * horizontal
    print(mutliply_result)

    file.close()
