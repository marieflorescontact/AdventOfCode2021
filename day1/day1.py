def main():
    path = 'day1.txt'
    file = open(path, 'r')
    depths = []
    for line in file:
        depths.append(int(line))

    increase = 0
    sum = []
    for i in range(len(depths) - 2):
        sum_of_3 = depths[i] + depths[i + 1] + depths[i + 2]
        sum.append(sum_of_3)

    for j in range(len(sum) - 1):
        if sum[j + 1] - sum[j] > 0:
            increase += 1
    print(increase)

    file.close()
