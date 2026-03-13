

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

def setup_exception_handlers(app: FastAPI):
    @app.exception_handler(Exception)
    async def global_handler(request: Request, exc: Exception):
        print(f"Hệ thống gặp lỗi: {exc}")
        return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "status": "fail",
            "message": "Đã xảy ra lỗi hệ thống. Vui lòng thử lại sau."
        },
    )