import discord
import random



class ClientComoSeDice(discord.Client):

    user: discord.ClientUser

    async def on_ready(self):
        print(f'Logged in as {self.user} [id: {self.user.id}]')
        print('---')
