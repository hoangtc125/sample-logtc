from fastapi import APIRouter

from app.services.test import TestServices
from logtc.logger import Logtc

router = APIRouter()


@router.get("/high")
async def high():
    Logtc().logger.info(f" - route /high")
    # raise Exception()
    return await TestServices().high()


@router.get("/medium")
async def medium():
    Logtc().logger.info("route /medium")
    return await TestServices().medium()


@router.get("/low")
async def low():
    Logtc().logger.info("route /low")
    return await TestServices().low()
