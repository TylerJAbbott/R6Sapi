#!/usr/bin/python3

import asyncio
import r6sapi as api

@asyncio.coroutine
def run():
    auth = api.Auth("tylerabbottthss@gmail.com", "Chandra66")
    
    usernames = ["assassin1901", "Pesto1911"]

    for username in usernames:
            player = yield from auth.get_player(username, api.Platforms.UPLAY)
            operator = yield from player.load_general()
            print(player.kills)

asyncio.get_event_loop().run_until_complete(run())
