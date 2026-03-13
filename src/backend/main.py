from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from injector import Injector
import uvicorn

from dependency import Dependencies
from fastapi_injector.request_scope import RequestScopeOptions
from middleware.exceptions import setup_exception_handlers
from scheduler.setup import setup_scheduler
from api.routers import routers as v1_routers

injector = Injector(Dependencies)
options = RequestScopeOptions(enable_cleanup=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Chạy Scheduler
    scheduler = setup_scheduler(injector, options=options)
    
    yield
    
    # Shutdown
    scheduler.shutdown()

# Thiết lập FastAPI
app = FastAPI(title="RimuSmart API",
              lifespan=lifespan)

# Add routers
app.include_router(v1_routers)

# Gọi hàm đăng ký các handler
setup_exception_handlers(app)

@app.get("/")
def read_root():
    return {"message": "Chào mừng bạn đến với RimuSmart!", "status": "running"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# Khối lệnh này cho phép bạn Debug trực tiếp bằng cách chạy file python
if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=False,  # Tự động tải lại khi code thay đổi
        log_level="info"
    )
