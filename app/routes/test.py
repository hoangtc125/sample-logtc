from fastapi import APIRouter

from app.services.test import TestServices
from logngo import Logger

router = APIRouter()


@router.get("/high")
async def high():
    Logger().logger.info(f" - route /high")
    # raise Exception()
    return await TestServices().high()


@router.get("/medium")
async def medium():
    Logger().logger.info("route /medium")
    return await TestServices().medium()


@router.get("/low")
async def low():
    Logger().logger.info("route /low")
    return await TestServices().low()
