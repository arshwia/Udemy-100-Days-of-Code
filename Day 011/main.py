import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def choice_card():
    return random.choice(cards)


def calculate_score(hand):
    score = sum(hand)

    # Blackjack
    if score == 21 and len(hand) == 2:
        return 0

    # Ace = 11 -> 1
    while score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score


def started_cards():
    return {
        "player": [choice_card(), choice_card()],
        "dealer": [choice_card(), choice_card()],
    }


def comparison(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "You lose. Dealer has Blackjack."
    elif player_score == 0:
        return "You win with Blackjack!"
    elif player_score > 21:
        return "You went over. You lose."
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose."


def dealer_turn(dealer_cards):
    dealer_score = calculate_score(dealer_cards)

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(choice_card())
        dealer_score = calculate_score(dealer_cards)

    return dealer_score


def main():
    game = started_cards()

    player_cards = game["player"]
    dealer_cards = game["dealer"]

    playing = True

    while playing:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"\nYour cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            playing = False
            break

        another = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another == "y":
            player_cards.append(choice_card())
        else:
            playing = False

    if player_score <= 21 and player_score != 0:
        dealer_score = dealer_turn(dealer_cards)

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print("\nFinal Results")
    print(f"Your cards: {player_cards}, final score: {player_score}")
    print(f"Dealer cards: {dealer_cards}, final score: {dealer_score}")

    print(comparison(player_score, dealer_score))


while True:
    play = input("Do you want to play Blackjack? (y/n): ").lower()

    if play == "y":
        main()
    else:
        print("Goodbye!")
        break
