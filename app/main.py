from fastapi import FastAPI
from . import config


app = FastAPI()
settings = config.get_settings()
print(settings)

@app.get("/")
async def homepage():
    return {"Hello":"World", "keyspace":settings.keyspace, "id":settings.client_id, "secret":settings.client_secret}