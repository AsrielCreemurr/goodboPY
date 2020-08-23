#imports; look for networking options/gui??
import random
onedeck = ["acedde1","2dde1","3dde1","4dde1","5dde1","6dde1","7dde1","8dde1","9dde1","tendde1","jackdde1","queendde1","kingdde1","acesde1","2sde1","3sde1","4sde1","5sde1","6sde1","7sde1","8sde1","9sde1","tensde1","jacksde1","queensde1","kingsde1","acehde1","2hde1","3hde1","4hde1","5hde1","6hde1","7hde1","8hde1","9hde1","tenhde1","jackhde1","queenhde1","kinghde1","acecde1","2cde1","3cde1","4cde1","5cde1","6cde1","7cde1","8cde1","9cde1","tencde1","jackcde1","queencde1","kingcde1"]
onedeckclassic = onedeck.copy()
onedeckclassic.append("joker1de1")
onedeckclassic.append("joker2de1")
versionselecting = 0
decktemp = []
valid = "placeholder"
valuethingy = "placeholder"
#TODO: ADD COMMENTS, REMOVE JUNK/DEBUGGING STUFF
def clear():
    print('\n' * 100)
def createdecks(decks,version):
    global deck
    global decktemp
    global temp
    if version == "official":
        print("Deck creation for official ruleset not created yet; try later.")
    elif version == "classic":
        decknumber = int(decks)
        while decknumber > 1:
            decktoadd = onedeckclassic.copy()
            strdecknumber = str(decknumber)
            decktoadd = [s.replace('de1',"de%s" % strdecknumber) for s in decktoadd]
            decktemp = decktemp + decktoadd
            decknumber = decknumber - 1
        deck = decktemp
def populategoalpiles():
    global deck
    global playergoals
    for i in playergoals:
        iteration = 0
        while iteration < intgcount:
            i.insert(0, deck[0])
            del(deck[0])
            iteration = iteration + 1
def populateplayhand(p):
    global deck
    global playerplaycards
    cardcount = len(playerplaycards[p])
    cardstoadd = 5 - cardcount
    for c in range(cardstoadd):
        try:
            playerplaycards[p].insert(0, deck[0])
            del (deck[0])
        except:
            print("Deck is empty.")
def display(p):
    clear()
    print("Topmost cards of all playpiles:")
    for d in playpiles:
        try:
            if valuefind(d[0]) == 20:
                print(d[0] + "(value = " + wildcheck(d,'m'))
            print(d[0])
        except:
            print("Empty pile")
    for r in range(intpcount):
        if r == p:
            print("Player " + str(r + 1) + "'s cards (YOU!!)")
            print("Goal:" + str(playergoals[r][0]) + "     Discards:" + str(playerdiscards[r]))
        else:
            print("Player " + str(r + 1) + "'s cards")
            print("Goal:" + str(playergoals[r][0]) + "     Discards:" + str(playerdiscards[r]))
    print("Your hand: " + str((playerplaycards[p])))
def valuefind(x):
    if x[0] == "a":
        return(1)
    elif x[0] == "t":
        return(10)
    elif x[0:2] == "ja":
        return(11)
    elif x[0] == "q":
        return(12)
    elif x[0] == "k":
        return(20)
    elif x[0:2] == "jo":
        return(20)
    else:
        return(int(x[0]))
def wildcheck(pile,mode):
    global wilditerable
    global playpiles
    if mode == "m":
        return(pile.len())
    elif mode == 'd':
        goodgoopie = 0
        while goodgoopie == 0:
            for c in pile:
                if valuefind(c) != 20:
                    returnedvalue = valuefind(c)
                    goodgoopie = 1
        return(returnedvalue)
def tuckstuff():
    global playerplaycards
    global playergoals
    tuckedcard = input("What card out of your hand would you like to tuck to the bottom of your goal pile??")
    for c in playerplaycards[playerplaying]:
        if c == tuckedcard: #TODO: CHECK IF WORKS, CHECK LIST METHS IF DOESNT
            playergoals[playerplaying].append(c)
            playerplaycards[playerplaying].remove(c)
def checkifvalid(card, mode):
    global value
    global valid
    global validpile
    cardvalue = valuefind(card)
    if mode == "move":
        manualstate = input("Would you like to manually place your card? (Y or N)")
        if manualstate.lower() == "y":
            attemptedpile = input("Type the top card of the pile you would like to manipulate")
            for p in playpiles:
                if p[0] == attemptedpile:
                    pilevalue = valuefind(p[0])
                    if pilevalue == 20:
                        pilevalue = wildcheck(p, 'm')
                    if cardvalue == pilevalue + 1:
                        valid = 1
                        validpile = p
                    elif cardvalue == 20:
                        valid = 1
                        validpile = p
                    else:
                        valid = 0
        else:
            for p in playpiles:
                if p:
                    pilevalue = valuefind(p[0])
                    if pilevalue == 20:
                        pilevalue = wildcheck(p, 'm')
                    if cardvalue == pilevalue + 1:
                        valid = 1
                        validpile = p
                    elif cardvalue == 20:
                        valid = 1
                        validpile = p
                    else:
                        valid = 0
                elif not p:
                    if cardvalue == 1:
                        valid = 1
                        validpile = p
                    elif cardvalue == 20:
                        valid = 1
                        validpile = p
                    else:
                        valid = 0
    elif mode == "discard":
        manualstate = input("Would you like to manually discard your card? (Y or N)")
        if manualstate.lower() == "y":
            attemptedpile = input("Type the top card of the pile you would like to manipulate")
            testiter = 0
            for g in playerdiscards[playerplaying]: #TODO: when tuck should occur, it instead places card into last player's discard; i suspect that when it iterates, it goes past the end of the current player's discard
                testiter = testiter + 1
                if testiter == 5:
                    print("Pile not found")
                elif g == attemptedpile:
                    try:
                        pilevalue = valuefind(g[0])
                        if pilevalue == 20:
                            pilevalue = wildcheck(g, 'd')
                        if cardvalue == pilevalue:
                            valid = 1
                            validpile = g
                        elif cardvalue == 20:
                            valid = 1
                            validpile = g
                        elif pilevalue == 0:
                            valid = 1
                            validpile = g
                        else:
                            print("Card can't be placed...")
                    except:
                        print("TUCK TIME!!!")
                        tuckstuff()
        else:
            testiter = 0
            for g in playerdiscards[playerplaying]:
                testiter = testiter + 1
                if testiter == 5:
                    #idea; set it to test if any valid discards upon calling discard function; tuck if needed
                    break
                try:
                    try:
                        pilevalue = valuefind(g[0])
                    except:
                        pilevalue = 0
                    if pilevalue == 20:
                        pilevalue = wildcheck(g, 'd')
                    if cardvalue == pilevalue:
                        valid = 1
                        validpile = g
                    elif cardvalue == 20:
                        valid = 1
                        validpile = g
                    elif pilevalue == 0:
                        valid = 1
                        validpile = g
                except:
                    print("TUCK TIME!!!")
                    tuckstuff()

    else:
        print("mode not specified; checkifvalid")
def playstuff(p):
    global deck
    global playerplaycards
    global playpiles
    global playerdiscards
    global playergoals
    global valid
    global validpile
    turnon = 1
    while turnon == 1:
        display(p)
        move = input("Please type in your move: \'place\', \'p\' or \'discard\', \'d\'")
        if move == "place" or move == "p":
            cardmove = input("Please type the name of the card that you would like to move.")
            #options = [playerplaycards[p], playerdiscards, playergoals]
            for c in playerplaycards[p]:
                if cardmove == c:
                    checkifvalid(cardmove, 'move')
                    print(valid)
                    if valid == 1:
                        playerplaycards[p].remove(c)
                        validpile.insert(0, cardmove)
            for g in playerdiscards:
                for c in g:
                    for l in c:
                        if cardmove == l:
                            checkifvalid(cardmove, 'move')
                            if valid == 1:
                                c.remove(l)
                                validpile.insert(0, cardmove)
                                display(p)
            for player in playergoals:
                if cardmove == player[0]:
                    checkifvalid(cardmove, 'move')
                    if valid == 1:
                        validpile.insert(0, cardmove)
                        player.remove(player[0])
                        display(p)
            if valuefind(validpile[0]) == 12:
                print("Pile ended!")
                for c in validpile:
                    deck.append(c)
                    validpile.remove(c)
        elif move == "discard" or move == "d":
            carddis = input("Please type the name of the card in your hand that you would like to discard.")
            for c in playerplaycards[p]:
                if c == carddis:
                    checkifvalid(carddis, 'discard')
                    if valid == 1:
                        playerplaycards[p].remove(c)
                        validpile.insert(0, carddis)
                        turnon = 0
                    else:
                        print("Not valid bro, that's kinda cringe ngl")
def main():
    print("Skipbo v1 is loading")
    global deck
    global decktemp
    global playergoals
    global intgcount
    global playerdiscards
    global playerplaycards
    global playpiles
    global intpcount
    global playerplaying
    versionselecting = 1
    while versionselecting: #LOOP TO DETERMINE RULESET IN PLAY
        versionselecting = 0
        versioni = input("Which version of Skip-Bo would you like to play; Official (bad), Classic, or Classic-2?")
        if versioni.lower() == "official":
            version = "official"
        elif versioni.lower() == "off":
            version = "official"
        elif versioni.lower() == "o":
            version = "official"
        elif versioni.lower() == "classic":
            version = "classic"
        elif versioni.lower() == "class":
            version = "classic"
        elif versioni.lower() == "c":
            version = "classic"
        elif versioni.lower() == "classic-2":
            version = "classic2"
        elif versioni.lower() == "classic2":
            version = "classic2"
        elif versioni.lower() == "c2":
            version = "classic2"
        else:
            versionselecting = 1
            print("Invalid selection; try 'official', 'classic', or 'classic2'.")
    if version == "official":
        print ("Playing by official Skip-Bo ruleset.")
        #IMPLEMENT
        print ("WIP; Asriel has yet to implement such a bad ruleset; perhaps another day.")
        exit()
    elif version == "classic":
        print ("Playing by classic (good) ruleset.")
        deckcount = input("How many decks would you like to use (2 is highly recommended unless playing with more than 4 people).")
        #MAKE MAX OF 50 DECKS FOR WEBSITE
        while deckcount.isnumeric() != 1 | int(deckcount) < 1 | deckcount.isdecimal() != 0:
            deckcount = input("Type a whole number greater than 0, please.")
        if deckcount == 1:
            print ("Shuffling deck...")
            deck = onedeckclassic.copy()
            deck = random.shuffle(deck)
        else:
            print ("Shuffling decks...")
            deck = onedeckclassic.copy()
            decktemp = onedeckclassic.copy()
            createdecks(deckcount,version)
            deck = random.shuffle(decktemp)
            deck = decktemp
        playercount = input("How many people are playing? Maximum 20 players") #How many players?
        while playercount.isnumeric() != 1 | int(playercount) <= 1 | playercount.isdecimal() != 0:
            playercount = input("Type a whole number greater than 0, please.")
        maxgoalpile = int(deckcount) * 60 / int(playercount) / 2 #How many cards are in the "goal pile"
        goalpilecount = input("How many cards are in the goal-pile? For this combination of decks and players, the maximum is %d. 15-30 is recommended." % maxgoalpile)
        while goalpilecount.isnumeric() != 1 | int(goalpilecount) <= 1 | goalpilecount.isdecimal() != 0:
            goalpilecount = input("Type a whole number greater than 0, please.")
        satisfied = input("If you would like to put in new settings, type 'exit' or 'quit' and start Skip-Bo again.. Otherwise, type anything and hit enter to begin your game.")
        #Check if user wants to quit/restart (I need to look for a better way of doing this, preferably one that can constantly run)
        if satisfied.lower() == "quit":
            exit
        elif satisfied.lower() == "exit":
            exit
        intpcount = int(playercount) #Create a variable of playercount that can be used
        intgcount = int(goalpilecount) #Create usable gpilecount
        playerhands = [{} for i in range(intpcount)] #Create a list holding the hands for x players
        playergoals = [[] for i in range(intpcount)] #Create a list holding the goalpiles of all players
        playerdiscards = [[[] for i in range(4)] for i in range(intpcount)] #Create a list holding the discard piles of players; indexed by player number, each "pile" is a list holding discard lists
        playerplaycards = [[] for i in range(intpcount)]  # Create a list holding the play cards
        oogabooga = 0
        for h in playerhands:
            h.update({"GoalPile":playergoals[oogabooga]}) #Append each playerhand to have key 'goalpile' corresponding to their index in playergoals
            h.update({"DiscardPiles":playerdiscards[oogabooga]}) #Same, but with discard piles
            h.update({"PlayCards":playerplaycards[oogabooga]})  # Same, but with playcards
            oogabooga = oogabooga + 1 #Iterate for loop, probably a simpler way to do this
        populategoalpiles() #<<<<
        #Note: this was a huge point in the coding process for me, because it took a hot minute to figure out how to get lists dynamically created n shit - seems simple from here
        print("The game has begun; players will take turns in ascending order of player number - 1,2,3,4,etc")
        playpiles = [[] for n in range(4)] #Creates 4 playpiles; the stuff ppl put cards on
        gameinsession = 1
        while gameinsession == 1:
            for p in range(intpcount):
                playerplaying = p
                populateplayhand(p)
                input("Press enter to continue; the following screen for " + str(p + 1) + "'s eyes only!")
                playstuff(p)
    elif version == "classic2": #IDENTICAL TO CLASSIC, USE DIFFERENT DECK
        print ("Playing by classic ruleset without jokers; two wildcards per deck is removed from play.")
main()