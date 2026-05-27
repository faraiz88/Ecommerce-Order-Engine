from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


async def http_error(
    request: Request,
    exc: HTTPException
):

    return JSONResponse(
        status_code=exc.status_code,

        content={
            "success": False,
            "detail": exc.detail
        }
    )


async def generic_error(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,

        content={
            "success": False,
            "detail":
            "Internal server error"
        }
    )