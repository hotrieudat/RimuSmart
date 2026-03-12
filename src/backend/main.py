from fastapi import FastAPI
import uvicorn

app = FastAPI(title="RimuSmart API")

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
