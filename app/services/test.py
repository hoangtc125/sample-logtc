import asyncio

from app.utils.test import high, medium, low
from logngo import Logger

class TestServices:
    def __init__(self):
        pass

    async def high(self):
        Logger().logger.info("services high")
        return await high()

    async def medium(self):
        await asyncio.sleep(1)
        Logger().logger.info("services medium")
        return await medium()

    async def low(self):
        await asyncio.sleep(2)
        Logger().logger.info("services low")
        return await low()
