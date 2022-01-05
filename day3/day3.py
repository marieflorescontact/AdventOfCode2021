def main():
    path = 'day3.txt'
    file = open(path, 'r')
    epsilon_rate_arr = []
    gamma_rate_arr = []

    lines = []
    number_of_0 = 0
    number_of_1 = 0

    for line in file:
        lines.append(line)

    for i in range(len(lines[-1])):
        for line in lines:
            if line[i] == "0":
                number_of_0 += 1

            if line[i] == "1":
                number_of_1 += 1

        if number_of_0 > number_of_1:
            gamma_rate_arr.append("0")
            epsilon_rate_arr.append("1")

        else:
            gamma_rate_arr.append("1")
            epsilon_rate_arr.append("0")
        number_of_0 = 0
        number_of_1 = 0

    gamma_rate = "".join(gamma_rate_arr)
    epsilon_rate = "".join(epsilon_rate_arr)

    print(gamma_rate)
    print(epsilon_rate)
    result = int(epsilon_rate, 2) * int(gamma_rate, 2)
    print(result)

    file.close()
