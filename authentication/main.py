from fastapi import FastAPI
from database import init_db
import routes as authentication
from contextlib  import asynccontextmanager
from dotenv import load_dotenv

@asynccontextmanager
async def lifespan(app: FastAPI):
   load_dotenv()
   await init_db()
   yield     

app = FastAPI(lifespan=lifespan, root_path="/authentication")


app.include_router(authentication.router, tags=["authentication"])
