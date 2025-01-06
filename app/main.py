from fastapi import FastAPI
from . import config, db
from cassandra.cqlengine.management import sync_table
from app.users.models import User
from contextlib import asynccontextmanager

DB_SESSION = None

settings = config.get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    print("Hello World")
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)
    yield
    # Code to run on shutdown

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def homepage():
    return {"Hello":"World", "keyspace":settings.keyspace, "id":settings.client_id, "secret":settings.client_secret}

@app.get("/users")
async def list_users():
    users = User.objects.all().limit(10)
    return list(users)

