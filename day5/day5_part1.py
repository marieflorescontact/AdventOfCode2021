def main():
    path = 'day5.txt'
    lines = []
    f = open(path, 'r')
    line = f.readline()
    while line:
        line = line.strip('\n').split(' ')
        left = [int(x) for x in line[0].split(',')]
        right = [int(x) for x in line[2].split(',')]
        lines.append([left, right])
        line = f.readline()

    grid = [[0] * 1000 for i in range(1000)]
    #print(lines)
    for line in lines:
        if line[0][0] == line[1][0]:
            a = min(line[0][1], line[1][1])
            b = max(line[0][1], line[1][1])
            for i in range(a, b + 1):
                grid[line[0][0]][i] += 1

        elif line[0][1] == line[1][1]:
            a = min(line[0][0], line[1][0])
            b = max(line[0][0], line[1][0])
            for i in range(a, b + 1):
                grid[i][line[0][1]] += 1



    count = 0
    for row in grid:
        for element in row:
            if element >= 2:
                count += 1

    print(count)

    f.close()
