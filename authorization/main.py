
from fastapi import FastAPI
from database import init_db
import routes as authorization
from contextlib  import asynccontextmanager
from dotenv import load_dotenv

@asynccontextmanager
async def lifespan(app: FastAPI):
   load_dotenv()
   await init_db()
   yield     

app = FastAPI(lifespan=lifespan, root_path="/authorization")


app.include_router(authorization.router, tags=["authorization"])
