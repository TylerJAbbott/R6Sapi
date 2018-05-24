#!/usr/bin/env python3
import asyncio
import getpass
import r6sapi as api
print("LOGIN")
username = input("Account email: ")
password = getpass.getpass("Account password: ")
user = input("In-game user: ")

@asyncio.coroutine
def run():
        while True:
            auth = api.Auth(username, password)
            player = yield from auth.get_player(user, api.Platforms.UPLAY)
            operators = input("Choose an Operator: ")
            operator = yield from player.get_operator(operators)
            KD = operator.kills/operator.deaths
            WR = operator.wins/operator.losses
            stringer = "You have %s kills and %s deaths on %s ... %s K/D Ratio" % (operator.kills, operator.deaths, operators, KD)
            wowsers = "You have %s wins and %s losses on %s ... %s Win Ratio" % (operator.wins, operator.losses, operators, WR)
            print(stringer)

            print(wowsers)
            grande = yield from player.load_general()
            print(player.kills)
            region = "NA"
            ariana = yield from api.Rank(region)
            print(ariana.mmr)
            again = input("Another Operator? (Y/N)")
            if again == "n":
                break



    

asyncio.get_event_loop().run_until_complete(run())
