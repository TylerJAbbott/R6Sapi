#!/usr/bin/env python3
import asyncio
import getpass
import r6sapi as api

usernamerr = 0
pasword = 0
assassin1901 = "assassin1901"
Pesto1911 = "Pesto1911"
billy_yoyo = "billy_yoyo"
fruity_kiwi = "fruity_kiwi"
captain_anime69 = "captain_anime69"


email = usernamerr
password = pasword
usernames = [Pesto1911, assassin1901, billy_yoyo, fruity_kiwi, captain_anime69]

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]



@asyncio.coroutine
def run():
        auth = api.Auth(email, password)
        file = open("new.txt","w")
        for username in usernames:
            player = yield from auth.get_player(username, api.Platforms.UPLAY)
            operator = yield from player.load_general()
            kill = player.kills
            death = player.deaths
            win = player.matches_won
            loss = player.matches_lost

            file.write(str(kill) + ",")
            file.write(str(death) + ",")
            file.write(str(win) + ",")
            file.write(str(loss) + ",")
        file.close()

        file = open("new.txt","r")
        lines = file.readlines()
        file.close()

        listing = []

        for line in lines:
            data = line.split(",")
            for temp in data:
                listing.append(temp)

        print(listing)

        file = open("old.txt","r")
        liners = file.readlines()
        file.close()

        lister = []

        for line in liners:
            data = line.split(",")
            for temp in data:
                lister.append(temp)

        print(lister)

        lister.pop()
        listing.pop()

        listing = [int(i) for i in listing]
        lister = [int(i) for i in lister]

        print(lister)
        print(listing)
       
        compared = []

        count = 0
        for b in lister:
            value = listing[count] - b
            count += 1
            compared.append(value)
        print(compared)

        sorted = list(chunks(compared, 4))

        print(sorted)

        arrayOfKills = []
        counter = 0
        for i in sorted:
            arrayOfKills.append(sorted[counter][0])
            counter += 1
            
        print(arrayOfKills)
        bestKiller = max(arrayOfKills)
        indexBestKiller = arrayOfKills.index(bestKiller)
        print(indexBestKiller)
        
        arrayOfDeaths = []
        counter0 = 0
        for i in sorted:
            arrayOfDeaths.append(sorted[counter0][1])
            counter0 += 1
        bestDeath = max(arrayOfDeaths)
        indexDeath = arrayOfDeaths.index(bestDeath)
        print(indexDeath)

        arrayOfWins = []
        counter1 = 0
        for i in sorted:
            if sorted[counter1][3] == 0:
                sorted[counter1][3] = 1
            arrayOfWins.append(sorted[counter1][2]/sorted[counter1][3])
            counter1 += 1
        bestWinner = max(arrayOfWins)
        indexWin = arrayOfWins.index(bestWinner)
        print(indexWin)

        arrayOfLosses = []
        counter2 = 0
        for i in sorted:
            arrayOfLosses.append(sorted[counter2][3])
            counter2 += 1
        bestLoser = max(arrayOfLosses)
        indexLoss = arrayOfLosses.index(bestLoser)
        print(indexLoss)

        arrayOfKDs = []
        counter3 = 0
        for i in usernames:
            if sorted[counter3][1] == 0:
                sorted[counter3][1] = 1
            arrayOfKDs.append(sorted[counter3][0]/sorted[counter3][1])
            counter3 += 1
        arrayOfKillRate = []
        counter4 = 0
        for i in usernames:
            temp = sorted[counter4][2]+sorted[counter4][3]
            if temp == 0:
                temp = 1
            arrayOfKillRate.append(sorted[counter4][0]/temp);
        file = open("printer.txt","w")
        ranger = len(arrayOfKDs)

        ranger = ranger
        for x in range(ranger):
            comma = ","
            needWrite = (str(usernames[x]) + comma)
            needing = (str(arrayOfKills[x]) + comma)
            needer = (str(arrayOfWins[x]) + comma)
            needs = (str(arrayOfKillRate[x]) + comma)
            needToWrite = (str(arrayOfKDs[x]) + comma)
            file.write(needWrite)
            file.write(needing)
            file.write(needer)
            file.write(needs)
            file.write(needToWrite)
        file.close()

        print(arrayOfKDs)
        print(usernames[indexBestKiller] + " is the best killer!")
        print(usernames[indexDeath] + " dies a whole lot.")
        print(usernames[indexWin] + " has won the most games.")
        print(usernames[indexLoss] + " has lost the most games.")

asyncio.get_event_loop().run_until_complete(run())
