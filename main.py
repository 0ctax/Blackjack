import random, os

cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "K", "Q"]
global deck
deck = []
global dealer
dealer = []
global dealt
dealt = []
global FirstRound
FirstRound = True
global Wins
Wins = 0
global Ties
Ties = 0
global Losses
Losses = 0

def Clear() :
    Clr = lambda: os.system('cls')
    Clr()

def Reset() :
    dealer.clear()
    dealt.clear()
    deck.clear()
    global FirstRound
    FirstRound = True

def CalculateScore(Side, Start) :
    if Side == "Dealer" :
        SideVar = dealer
    else :
        SideVar = dealt
    score = 0
    for i in SideVar :
        try :
            score+=int(i)
        except :
            if i != "A" :
                score+=10
        if Start and score != 0 :
            return score
    for i in SideVar :
        if i == "A" :
            if score + 11 > 21 :
                score+=1
            else :
                score+=11
            if SideVar.count("A") > 1 :
                for z in range(SideVar.count("A"), SideVar.count("A")) :
                    score-=10
        if Start and score != 0 :
            return score
    return score

def CurrentHand(Side, Start) :
    if Side == "Dealer" :
        SideVar = dealer
    else :
        SideVar = dealt
    FinalHand = ""
    for i in SideVar :
        FinalHand = FinalHand + i + " "
        if Start :
            return FinalHand
    return FinalHand

def CreateDeck() :
    Loopcount = 0
    while Loopcount < 52 :
        Loopcount+=1
        deck.append(random.choice(cards))

def DrawCard(Side, Start) :
    card = deck[1]
    deck.remove(card)
    if Side == "Dealer" :
        dealer.append(card)
        if not Start :
            print("[+] Dealer dealt " + card)
    elif Side == "Dealt" :
        dealt.append(card)
        print("[+] You drew " + card)

def Intro() :
    Clear()
    Reset()
    CreateDeck()
    print("Wins : {}, Ties : {}, Losses : {}".format(Wins, Ties, Losses))
    print("\nWelcome to blackjack! Press Enter to start!")
    print("Dealer automatically stands at 17.\n")
    input()
    def Turn() :
        Clear()
        global Ties, Wins, Losses
        global FirstRound
        if CalculateScore("Dealt", False) == 0 :
            DrawCard("Dealt", False)
            DrawCard("Dealer", False)
            DrawCard("Dealt", False)
            DrawCard("Dealer", True)
        if CalculateScore("Dealer", False) == 21 :
            print("Blackjack! Dealer Wins!\n")
            input("Press Enter to go back to menu.")
            Losses+=1
            Intro()
        elif CalculateScore("Dealt", False) == 21 and FirstRound == True :
            print("Blackjack! You Win!\n")
            input("Press Enter to go back to menu.")
            Wins+=1
            Intro()
        elif CalculateScore("Dealt", False) > 21 :
            print("You went Bust! You Lose!\n")
            input("Press Enter to go back to menu.")
            Losses+=1
            Intro()
        else :
            FirstRound = False
            print("Your Cards : {}\nDealers Cards : {}\n{}\nDealers Score : {}\nYour Score : {}".format(CurrentHand("Dealt", False),CurrentHand("Dealer", True),"".join("-"*10), CalculateScore("Dealer", True), CalculateScore("Dealt", False)))
            print("\nPlease select an option : \n[H] Hit [S] Stand")
            Selection = input()
            if Selection.lower() == "s" or Selection.lower() == "h" :
                if Selection.lower() == "h" :
                    DrawCard("Dealt", False)
                    Turn()
                elif Selection.lower() == "s" :
                    Clear()
                    while CalculateScore("Dealer", False) < 17 :
                        DrawCard("Dealer", False)
                        print("Your Cards : {}\nDealers Cards : {}\n{}\nDealers Score : {}\nYour Score : {}".format(CurrentHand("Dealt", False),CurrentHand("Dealer", False),"".join("-"*10), CalculateScore("Dealer", False), CalculateScore("Dealt", False)))
                    if CalculateScore("Dealer", False) == CalculateScore("Dealt", False) :
                        print("Draw! It's a tie!")
                        Ties+=1
                        input("Press Enter to go back to menu.")
                        Intro()
                    elif CalculateScore("Dealer", False) > 21 :
                        print("Dealer went Bust! You Win!")
                        Wins+=1
                        input("Press Enter to go back to menu.")
                        Intro()
                    elif CalculateScore("Dealer", False) > CalculateScore("Dealt", False) :
                        print("The Dealer has {}. You Lose!".format(CalculateScore("Dealer", False)))
                        Losses+=1
                        input("Press Enter to go back to menu.")
                        Intro()
                    elif CalculateScore("Dealer", False) < CalculateScore("Dealt", False) :
                        print("Dealer Lost! You Win!")
                        Wins+=1
                        input("Press Enter to go back to menu.")
                        Intro()
            else :
                Turn()
    Turn()

Intro()