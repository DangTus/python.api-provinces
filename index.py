from fastapi import FastAPI

from controllers.tinh_thanh import get_tinh_thanh
from controllers.quan_huyen import get_quan_huyen


app = FastAPI()


@app.get("/tinh-thanh")
def tinh_thanh():
    return get_tinh_thanh()


@app.get("/quan-huyen")
def quan_huyen(tt_code: int, tt_codename: str = None, tt_phonecode: int = None):
    return get_quan_huyen(tt_code, tt_codename, tt_phonecode)
