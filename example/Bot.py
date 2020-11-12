import discord
from discord.ext import commands
from Naver_Api.Api import Naver

bot = commands.Bot(command_prefix="!")

client_id = "네이버 Api 클라이언트 ID"
client_secret = "네이버 Api 시크릿 ID"

N = Naver(client_id, client_secret)


@bot.event
async def on_ready():
    print(f"{bot.user.name} 준비 완료.")


@bot.command()
async def 영화(ctx, *, query):
    a = await N.Movie(query=query)
    for i in a["items"]:
        director = i["director"]
        direct = str(director).replace("|", "\n")
        actor = i["actor"]
        act = str(actor).replace("|", "\n")
        embed = discord.Embed(title=i["subtitle"])
        embed.add_field(name="개봉일", value=i["pubDate"])
        embed.add_field(name="감독", value=direct)
        embed.add_field(name="배우", value=act)
        embed.set_thumbnail(url=i["image"])
        embed.add_field(name=f"[자세한 내용 보러가기]({i['link']})", value="")
        embed.add_field(name="평점", value=i["userRating"])
        await ctx.send(embed=embed)


bot.run("Your Token")
