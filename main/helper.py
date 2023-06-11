import json
import asyncio
from aiohttp import ClientSession


async def get_available_lots(session, url):
    """
    Retrieves available parking lots
    """

    response = await session.get(url=url)

    if response.status == 200:
        return await response.json()
    else:
        print(f'failed to retrieve file from {url}')
