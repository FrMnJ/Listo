from fastapi import FastAPI
from database import init_db
import routes as auth
from contextlib  import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
   await init_db()
   yield     

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
