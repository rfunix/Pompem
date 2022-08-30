import socket

import aiohttp
import async_timeout

TIMEOUT = 120

headers = {
    "User-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "referer": "https://www.google.com",
}


async def request_worker(url):
    async with aiohttp.ClientSession() as session:
        return await fetch(session, url)


async def fetch(session, url):
    with async_timeout.timeout(TIMEOUT):
        async with session.get(url, headers=headers) as response:
            return await response.text()


async def request_worker_keep_session(url, session_url, data):
    conn = aiohttp.TCPConnector(family=socket.AF_INET, verify_ssl=False)

    async with aiohttp.ClientSession(connector=conn) as session:
        return await fetch_keep_session(session, url, data, session_url)


async def fetch_keep_session(session, url, data, session_url):
    with async_timeout.timeout(TIMEOUT):
        async with session.post(session_url, data=data, headers=headers):
            async with session.get(url, headers=headers) as response:
                return await response.text()
