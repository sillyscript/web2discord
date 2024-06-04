import json
import aiohttp
import asyncio
from scraper import scrape
from checker import checkIfNew
from discordsend import send_embed

with open("config.json") as f:
    data = json.load(f)
    hUrl = data['discord']

def getUrl(urlType: str):
    with open("config.json") as f:
        data = json.load(f)
    url = data[urlType]
    return url

async def noticeFinder(site: str):
    consecutiveError = 0
    while consecutiveError < 5:
        if site == "cupgs":
            url = getUrl("cupgsUrl")
        elif site == "main":
            url = getUrl("newsUrl")
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        for noticeNum in range(15):
                            ref, title, link, date = scrape(await response.text(), noticeNum + 1)
                            newbie = checkIfNew(title)
                            if newbie:
                                await send_embed(hUrl, ref + ": " + title if ref else title, link, date)
                                consecutiveError = 0
                                print(f"Sent: {title}")
                    else:
                        print("Failed Response")
                        consecutiveError += 1
            except Exception as e:
                print(f"An error occurred: {e}")
                consecutiveError += 1
        
        if consecutiveError >= 5:
            print("\nStopping program due to frequent crashes in system!")
            return
        await asyncio.sleep(60)

async def main():
    while True:
        await noticeFinder("main")
        await asyncio.sleep(60 * 15)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
