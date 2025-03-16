import asyncio
import re

import aiohttp

PATTERN = re.compile(r"\<title\>(?P<title>.*)\<\/title\>")


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group("title"))


def main():
    urls = (
        "https://www.python.org/",
        "https://git-scm.com/",
        "https://www.jd.com/",
        "https://www.taobao.com/",
        "https://www.douban.com/",
    )
    loop = asyncio.get_event_loop()
    cos = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(cos))
    loop.close()


if __name__ == "__main__":
    main()


"""
1. 实际开发过程中要提升系统的可扩展性和并发性同场有垂直亏哦站（增加单个节点的处理能力）
2. 水平扩展，将单个节点编程多个节点

可以通过消息队列来实现应用程序的耦合，
    * 消息队列相当于多线程同步队列的扩展版本
    * 不同机器上的应用程序相当于线程


"""

