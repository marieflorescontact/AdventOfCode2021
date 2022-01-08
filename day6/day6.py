def main():
    path = 'day6.txt'
    states = []
    f = open(path, 'r')
    for line in f:
        states.append(line.split(','))

    for i in range(80):
        new_state = []
        new_fish = []
        for j in range(len(states[i])):
            internal_timer = int(states[i][j])
            internal_timer -= 1
            if internal_timer < 0:
                internal_timer += 7
                new_fish.append('8')

            new_state.append(str(internal_timer))
        states.append(new_state + new_fish)

    last_day = states[-1]
    fishes = len(last_day)
    print(fishes)

    f.close()
