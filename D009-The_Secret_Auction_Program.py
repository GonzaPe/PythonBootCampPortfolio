#from replit import clear
#the program should run with this import but I can't find the file, so is not so secret.
#from art import logo

#print(logo)
print("Welcome to the blind auction program.")
bid_history = {}
more_biders = True
winner = ""
def find_max_bid(bid_records):
    maxbid = 0
    for name in bid_records:
        price = bid_records[name]
        if maxbid < price:
            maxbid = price
            winner = name
    print(f"The winner is {winner} with an offer of ${maxbid}")

while more_biders == True:
    name=str(input("Please enter the bidders name: "))
    price=int(input("Please enter the bid: $"))
    bid_history[name] = price
    should_continue = input("Is there any other bidder? (type yes/no): ")
    if (should_continue == "no"):
        more_biders = False
        find_max_bid(bid_records=bid_history)
    #replit.clear
