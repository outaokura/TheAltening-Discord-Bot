import discord
import discord.app_commands
import requests

token = "YOUR TOKEN" #BOT TOKEN
key = "api-1919-4545-0721" # ALTENING API
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@tree.command(
    name="alt",
    description="Generate alt token"
)
async def hoge(ctx:discord.Interaction):
    res = requests.get(f'https://api.thealtening.com/v2/generate?key={key}')
    token = res.json()["token"]
    username = res.json()["username"]
    exp = res.json()["expires"]
    exp = exp.replace("T", " ")
    char = "."
    expires = exp[:exp.index(char)] if char in exp else exp
    embed=discord.Embed(title="TheAltening Token Generator", color=0x1ab725)
    embed.add_field(name="Token", value=f"```{token}```", inline=False)
    embed.add_field(name="Username", value=f"```{username}```", inline=True)
    embed.set_footer(text=f"このTokenは{expires}に無効になります")
    await ctx.response.send_message(embed=embed)

@client.event
async def on_ready():
    print("ready")
    await tree.sync()
client.run(token)
