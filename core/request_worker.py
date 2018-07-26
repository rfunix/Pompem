import aiohttp
import async_timeout

TIMEOUT = 60

async def fetch(session, url):
    with async_timeout.timeout(TIMEOUT):
        async with session.get(url) as response:
            return await response.text()


async def request_worker(url):
    async with aiohttp.ClientSession() as session:
        return await fetch(session, url)


async def request_worker_keep_session(url, session_url, data):
    async with aiohttp.ClientSession() as session:
        return await fetch_keep_session(session, url, data, session_url)


async def fetch_keep_session(session, url, data, session_url):
    with async_timeout.timeout(TIMEOUT):
        async with session.post(session_url, data=data):
            async with session.get(url) as response:
                return await response.text()
