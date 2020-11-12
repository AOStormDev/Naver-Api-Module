from Naver_Api.Api import Naver
import asyncio

client_id = "클라이언트 ID"
client_secret = "클라이언트 시크릿"

N = Naver(client_id, client_secret)


async def Console():
    print(await N.ShortUrl(url="https://freeai.me"))


asyncio.run(Console())