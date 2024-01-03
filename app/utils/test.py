import asyncio
from logtc.logger import Logtc


async def high():
    Logtc().logger.info("utils high")
    return "success"


async def medium():
    await asyncio.sleep(1)
    Logtc().logger.info("utils medium")
    return "success"


async def low():
    await asyncio.sleep(2)
    Logtc().logger.info("utils low")
    return "success"
