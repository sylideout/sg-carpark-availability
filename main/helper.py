import json
import asyncio


async def get_available_lots(session, url):
    """
    Retrieves available parking lots
    """

    response = await session.get(url=url)

    if response.status == 200:
        res = await response.json()
        return res
    else:
        print(f'failed to retrieve file from {url}')
