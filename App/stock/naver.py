from scrapy.selector import Selector
from Exts.Performance import Performance
import aiohttp
import re


class Stocks:
    def __init__(self):
        self.loop = Performance()
        self.url = "https://m.stock.naver.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10.0.0; SM-G988NZKAKOO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
        }

    async def cleanText(self, text):
        loop = Performance()
        # cleanT = await loop.run_in_executor(None, re.sub, "<.+?>", "", str(text), 0, re.I|re.S)
        cleanT = await loop.run_in_threadpool(lambda: re.sub("<.+?>", "", str(text), 0, re.I|re.S))
        return cleanT

    async def Request(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.url) as resp:
                if resp.status != 200:
                    raise Exception("404 Not Found")
                html = await resp.text()
        soup = await self.loop.run_in_threadpool(lambda: Selector(text=html))
        return soup

    async def KOSPI(self):
        """코스피"""
        soup = await self.Request()

        kospi = await self.loop.run_in_threadpool(lambda: soup.xpath('//*[@id="mflick"]/div/div[1]/div/ul/li[1]/a/div[1]/span'))
        u_kospi = await self.loop.run_in_threadpool(lambda: soup.xpath('//*[@id="mflick"]/div/div[1]/div/ul/li[1]/a/div[1]/div'))

        _kospi = await self.loop.run_in_threadpool(lambda: kospi.getall()[0])
        _u_kospi = await self.loop.run_in_threadpool(lambda: u_kospi.getall()[0])

        clean = await self.cleanText(_kospi)

        clean2 = await self.cleanText(_u_kospi.strip().replace('<span class="gap_rate">', '^').replace("</em>", '^'))

        return f"코스피: {clean.strip()},    {clean2.strip().replace('^', '   ')}"

    async def KOSDAQ(self):
        """코스닥"""
        soup = await self.Request()

        kosdaq = await self.loop.run_in_threadpool(lambda: soup.xpath('//*[@id="mflick"]/div/div[1]/div/ul/li[2]/a/div[1]/span'))
        u_kosdaq = await self.loop.run_in_threadpool(lambda: soup.xpath('//*[@id="mflick"]/div/div[1]/div/ul/li[2]/a/div[1]/div'))

        _kosdaq = await self.loop.run_in_threadpool(lambda: kosdaq.getall()[0])
        _u_kosdaq = await self.loop.run_in_threadpool(lambda: u_kosdaq.getall()[0])

        clean = await self.cleanText(_kosdaq)
        clean2 = await self.cleanText(_u_kosdaq.strip().replace('<span class="gap_rate">', '^').replace("</em>", '^'))

        return f"코스닥: {clean.strip()},    {clean2.strip().replace('^', '   ')}"
