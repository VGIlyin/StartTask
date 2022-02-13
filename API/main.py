from fastapi import FastAPI


app = FastAPI()


@app.get("/info")
async def get_info():
    return {"message": "info"}


@app.get("/post")
async def load_vm():
    return {"message": "current CPU is ..."}
