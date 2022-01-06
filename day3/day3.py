def main():
    path = 'day3.txt'
    file = open(path, 'r')

    ###PART 1#####
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

    result = int(epsilon_rate, 2) * int(gamma_rate, 2)

    # print(result)

    ###PART 2#####

    co2_scrub_rating = find_co2_rating(lines, number_of_0, number_of_1)
    oxygen_rating = find_oxygen_rating(lines, number_of_0, number_of_1)

    life_support_rating = int(oxygen_rating,2) * int(co2_scrub_rating,2)
    print(life_support_rating)

    file.close()


def find_co2_rating(lines, number_of_0, number_of_1):
    co2_scrub_rating=[]
    for i in range(len(lines[-1])):
        for line in lines:
            if line[i] == "0":
                number_of_0 += 1

            if line[i] == "1":
                number_of_1 += 1

        if number_of_0 > number_of_1:
            lines = list(filter(lambda line: line[i] == "1", lines))
            if len(lines) == 1:
                co2_scrub_rating = lines

        if number_of_0 < number_of_1:
            lines = list(filter(lambda line: line[i] == "0", lines))
            if len(lines) == 1:
                co2_scrub_rating = lines

        if number_of_0 == number_of_1:
            lines = list(filter(lambda line: line[i] == "0", lines))
            if len(lines) == 1:
                co2_scrub_rating = lines

        number_of_0 = 0
        number_of_1 = 0

    return co2_scrub_rating[0]

def find_oxygen_rating(lines, number_of_0, number_of_1):
    oxygen_rating =[]
    for i in range(len(lines[-1])):
        for line in lines:
            if line[i] == "0":
                number_of_0 += 1

            if line[i] == "1":
                number_of_1 += 1

        if number_of_0 > number_of_1:
            lines = list(filter(lambda line: line[i] == "0", lines))
            if len(lines) == 1:
                oxygen_rating = lines

        if number_of_0 < number_of_1:
            lines = list(filter(lambda line: line[i] == "1", lines))
            if len(lines) == 1:
                oxygen_rating = lines

        if number_of_0 == number_of_1:
            lines = list(filter(lambda line: line[i] == "1", lines))
            if len(lines) == 1:
                oxygen_rating = lines

        number_of_0 = 0
        number_of_1 = 0

    return oxygen_rating[0]
