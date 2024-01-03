import asyncio
from logngo import Logger

async def high():
    Logger().logger.info("utils high")
    return "success"


async def medium():
    await asyncio.sleep(1)
    Logger().logger.info("utils medium")
    return "success"


async def low():
    await asyncio.sleep(2)
    Logger().logger.info("utils low")
    return "success"
