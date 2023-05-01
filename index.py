from fastapi import FastAPI
from controllers.tinh_thanh import get_tinh_thanh


app = FastAPI()


@app.get("/tinh-thanh")
def tinh_thanh(code: int = None, codename: str = None, phone_code: int = None):
    return get_tinh_thanh(code, codename, phone_code)
