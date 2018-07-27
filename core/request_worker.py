import aiohttp
import async_timeout
import socks
import socket

TIMEOUT = 120
TOR_HOST = '127.0.0.1'
TOR_PORT = 9050


def use_tor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, TOR_HOST, TOR_PORT)
    socket.socket = socks.socksocket

    def getaddrinfo(*args):
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

    socket.getaddrinfo = getaddrinfo


headers = {
    'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'referer': 'https://www.google.com'
}


async def fetch(session, url):
    with async_timeout.timeout(TIMEOUT):
        async with session.get(url, headers=headers) as response:
            return await response.text()


async def request_worker(url):
    async with aiohttp.ClientSession() as session:
        return await fetch(session, url)


async def request_worker_keep_session(url, session_url, data):
    use_tor()
    async with aiohttp.ClientSession() as session:
        return await fetch_keep_session(session, url, data, session_url)


async def fetch_keep_session(session, url, data, session_url):
    with async_timeout.timeout(TIMEOUT):
        async with session.post(session_url, data=data, headers=headers):
            async with session.get(url, headers=headers) as response:
                return await response.text()
