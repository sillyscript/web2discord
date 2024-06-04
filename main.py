import json
import aiohttp
import asyncio
import time
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
    if site == "cupgs":
        url = getUrl("cupgsUrl")
    elif site == "main":
        url = getUrl("newsUrl")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                for noticeNum in range(15):
                    ref, title, link, date = scrape(await response.text(), noticeNum + 1)
                    newbie = checkIfNew(title)
                    if newbie:
                        await send_embed(hUrl, ref + ": " + {title} if ref else title, link, date)
                        
                
            else:
                print("Failed Response")
    time.sleep(1800)

loop = asyncio.get_event_loop()
loop.run_until_complete(noticeFinder("main"))
