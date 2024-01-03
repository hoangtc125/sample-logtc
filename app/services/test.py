import asyncio

from app.utils.test import high, medium, low
from logtc.logger import Logtc


class TestServices:
    def __init__(self):
        pass

    async def high(self):
        Logtc().logger.info("services high")
        return await high()

    async def medium(self):
        await asyncio.sleep(1)
        Logtc().logger.info("services medium")
        return await medium()

    async def low(self):
        await asyncio.sleep(2)
        Logtc().logger.info("services low")
        return await low()
