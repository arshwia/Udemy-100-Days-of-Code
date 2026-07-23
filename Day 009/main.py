from os import system


def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}

contnue_bidding = True
while contnue_bidding:
    name = str(input("What is your name?: ")).lower()
    price = int(input("What is your bid?: $"))

    bids[name] = price

    should_contnue = str(
        input("Are there any other bidders? Type 'yes or 'no'.\n  ")
    ).lower()

    if should_contnue == "no":
        contnue_bidding = False
        system("clear")
        find_highest_bidder(bids)
    elif should_contnue == "yes":
        system("clear")
