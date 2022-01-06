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
    #print(drawn)

    found = False
    while found == False:
        number = drawn[0]
        drawn = drawn[1:]
        for card in all_cards:
            for i in range(len(card)):
                if card[i] == number:
                    card[i] = 100

        for card in all_cards:
            if is_winner(card):
                total = sum([x for x in card if x != 100])

                result = total * number
                print(result)
                found = True

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
