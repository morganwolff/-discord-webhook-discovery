#!/usr/bin/python3
import asyncio
import csv

import discord
from discord import Webhook
import aiohttp


def read_file():
    csv_filename = 'datas/pandas.txt'
    with open(csv_filename) as f:
        reader = csv.reader(f)
        lst = list(reader)
    print(lst)
    return lst


async def send_elements():
    lst = read_file()
    for line in lst:
        await foo(line)
    return


async def foo(model):
    discord_webhook_url = 'https://discord.com/api/webhooks/1052979338280185856/BI1V1prW3N7F3MxT9gN56HU29DNI5MpLhn57IGfA8ZEv9xit6CHQBuGbqcNv8naf8dXR'
    titre = model[0]
    price = "PRICE: " + model[1] + "€\n"
    availability = model[2]
    couleur = discord.Color.red() if model[2] == 'Rupture de stock' else discord.Color.green()
    image_url = model[3]
    product_url = model[4]

    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(discord_webhook_url, session=session)
        emb = discord.Embed(title=titre, color=couleur, description=price + availability, url=product_url)
        emb.set_image(url=image_url)
        await webhook.send(embed=emb)


def main():
    asyncio.run(send_elements())


if __name__ == "__main__":
    main()
