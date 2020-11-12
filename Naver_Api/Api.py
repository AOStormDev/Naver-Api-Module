import aiohttp
import asyncio
import json


class Naver:
    def __init__(self, Client_Id, Client_Secret):
        self.url = "https://openapi.naver.com"
        self.headers = {
            "X-Naver-Client-Id": str(Client_Id),
            "X-Naver-Client-Secret": str(Client_Secret),
        }

    async def Movie(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/movie.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Blog(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/blog.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def News(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/news.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Book(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/book.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Adult(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/adult.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Encyc(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/encyc.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Cafe(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/cafearticle.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Kin(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/kin.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Local(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/local.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Errata(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/errata.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Webkr(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/webkr.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Image(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/image?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Shop(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/shop.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def Doc(self, query: str, display: int = None):
        if display == None:
            display = ""
        else:
            display = f"?display={display}"
        url = f"{self.url}/v1/search/doc.json?query={query}{display}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as f:
                return await f.json()

    async def ShortUrl(self, url: str):
        url = f"{self.url}/v1/util/shorturl.json"
        params = {"url": str(url)}
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers, params=params) as f:
                return await f.json()