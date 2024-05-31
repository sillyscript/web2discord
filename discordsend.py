import discord
from discord import Webhook
import asyncio, aiohttp


async def send_embed(webhook_url, notice_text, google_drive_link, notice_date):
	async with aiohttp.ClientSession() as session:
		webhook = Webhook.from_url(webhook_url, session=session)
		discord_embed = discord.Embed(color=0x00FF00, title = "Notice", description=notice_text, url=google_drive_link)
		discord_embed.set_footer(text=f"Published on: {notice_date}")
		discord_embed.set_thumbnail(url="https://media.discordapp.net/attachments/937333236214923304/1159095910236692520/Screenshot_2023_1004_172250.jpg?ex=651ea3af&is=651d522f&hm=3ff85e9c015715639bfdc34d48ad6c1a43ee685b2cf91f5440f23bce23ba8c4d&")
		await webhook.send(embed=discord_embed)

