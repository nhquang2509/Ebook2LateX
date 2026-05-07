# Goi thu vien FastAPI

from fastapi import FastAPI

# Tao doi tuong app tu class FastAPI

app = FastAPI()

# Tao decorator cho app.get(“/”) 

@app.get("/")

# khi nguoi dung truy cap vao web root, goi ham sau

def read_root():

    return {"message": "Chao mung ban den voi Ebook2LateX!"}

@app.get("/nhanvoi10")
def multiply_by_10(value: float):

    return {"result": value * 10}