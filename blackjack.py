import random

dealer_cards=[]
player_cards=[]

print("Hello, would you like to be the dealer or the player?(type 1 for dealer, 2 for player)")
mode=0
try:
    mode=int(input('Input:'))
except ValueError:
    print("Not a number")

if mode == 1:
    print("You are playing as the dealer.")
    while len(dealer_cards)!=2:
        dealer_cards.append(random.randint(1,11))
        if len(dealer_cards)==2:
            print("You have ", dealer_cards)


    while len(player_cards)!=2:
        player_cards.append(random.randint(1,11))
        if len(player_cards)==2:
            print("Player has ", player_cards)

    #Sum of dealer cards
    if sum(dealer_cards)==21:
        print("You have 21 and you won!")
    elif sum(dealer_cards)>21:
        print("You are busted!")

    while sum(player_cards)<21:
        action_taken = random.randint(1,2)
        if action_taken==1:
            print("Player has hit")
            player_cards.append(random.randint(1,11))
            print("Player has a total of "+str(sum(player_cards))+ " from these cards ",player_cards)
        else:
            print("Player is staying")
            print("Player has a total of "+str(sum(player_cards))+ " from these cards ",player_cards)
            break

    if sum(player_cards)>21:
        print("Player is BUSTED! You win!")
    else:
        while sum(dealer_cards) < 21:
            actionD = str(input("Dealer, do you hit or stay?"))
            if actionD == "hit":
                print("Dealer has hit")
                dealer_cards.append(random.randint(1, 11))
                print("Dealer has a total of " + str(sum(dealer_cards)) + " from these cards ", dealer_cards)
            else:
                print("Dealer is staying")
                print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                break

        if sum(dealer_cards)>21:
            print("Dealer is BUSTED! Player wins!")
        elif sum(dealer_cards)== sum(player_cards):
            print("You win!")
        elif sum(dealer_cards)==21:
            print("You have BLAKCJACK!")
        elif sum(player_cards)==21:
            print("Player has BLACKJACK!")
        elif sum(dealer_cards)>sum(player_cards):
            print("You win!")
        else:
            print("Player wins!")

else:
    print("You are the player")
    bet_choice =str(input("Player, do you want to bet? YES or NO:"))
    if bet_choice=="YES":
        bet_ammount = input("How much would you like to bet?")
    else:
        bet_ammount =0

    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print("Dealer has X &", dealer_cards[1])

    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 11))
        if len(player_cards) == 2:
            print("You have ", player_cards)

    if sum(dealer_cards) == 21:
        print("Dealer has 21 and wins!")
    elif sum(dealer_cards) > 21:
        print("Dealer has busted!")

    while sum(player_cards) <21:
        action_ta = str(input("Do you want to stay or hit? "))
        if action_ta == "hit":
            player_cards.append(random.randint(1, 11))
            print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
        else:
            print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
            break
    if sum(player_cards) > 21:
        print("Player is BUSTED! Dealer wins!")
    else:
        while sum(dealer_cards) < 21:
            daction = random.randint(1, 2)
            if daction == 1:
                print("Dealer has hit")
                dealer_cards.append(random.randint(1, 11))
            else:
                print("Dealer is staying")
                print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                break

        if sum(dealer_cards)>21:
            print("Dealer is BUSTED! Player wins!")
            if bet_ammount != 0:
                bet_ammount = int(bet_ammount) * 2
                print("You have won " + str(bet_ammount)+"$")
        elif sum(dealer_cards)== sum(player_cards):
            print("Dealer wins!")
        elif sum(dealer_cards)==21:
            print("Dealer has BLAKCJACK!")
        elif sum(player_cards)==21:
            print("You has BLACKJACK!")
            if bet_ammount != 0:
                bet_ammount = int(bet_ammount)* 2
                print("You have won " + str(bet_ammount)+"$")
        elif sum(dealer_cards)>sum(player_cards):
            print("Dealer wins!")
        else:
            print("You win!")
            if bet_ammount != 0:
                bet_ammount = int(bet_ammount) * 2
                print("You have won " + str(bet_ammount)+"$")

