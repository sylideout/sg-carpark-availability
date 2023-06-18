import asyncio
from helper import get_available_lots
from aiohttp import ClientSession

#to-do: update envvar on server
URL = "http://datamall2.mytransport.sg/ltaodataservice/CarParkAvailabilityv2?$skip="
API_KEY = "8pjsOFa5RpeLxuoRbBM2Eg=="


async def bulk_get(calls):
    """
    Calls get_available_lots concurrently
    """

    headers = {'AccountKey': API_KEY}

    async with ClientSession(headers=headers) as session:
        tasks = []
        for i in range(calls):
            suffix = str(i*500)
            task = asyncio.create_task(
                get_available_lots(session, URL+suffix)
                    )
            tasks.append(task)
        results = await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(bulk_get(6))
