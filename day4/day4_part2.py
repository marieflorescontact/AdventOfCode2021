def main():
    path = 'day4.txt'
    file = open(path, 'r')
    drawn = [int(x) for x in file.readline().strip('\n').split(',')]
    all_cards = []
    while file.readline():
        card = []
        for i in range(5):
            card.extend([int(x) for x in file.readline().strip('\n').split(' ') if x != ''])
        all_cards.append(card)
    # print(drawn)

    found = False
    while found == False:
        number = drawn[0]
        drawn = drawn[1:]
        for i in range(len(all_cards)):
            for j in range(len(all_cards[i])):
                if all_cards[i][j] == number:
                    all_cards[i][j] = 100

        i = 0
        while i < len(all_cards):
            if is_winner(all_cards[i]):
                if len(all_cards) > 1:
                    all_cards.pop(i)
                else:
                    found = True
                    print(all_cards[i])
                    break
            else:
                i += 1
    total = sum([x for x in all_cards[i] if x != 100])
    result = total * number
    print(result)

    file.close()


def is_winner(card):
    # horizontal rows
    start = 0
    for i in range(5):
        if card[start] + card[start + 1] + card[start + 2] + card[start + 3] + card[start + 4] == 500:
            return True
        start += 5

    # vertical columns
    start = 0
    for i in range(5):
        if card[start] + card[start + 5] + card[start + 10] + card[start + 15] + card[start + 20] == 500:
            return True
        start += 1

    return False
