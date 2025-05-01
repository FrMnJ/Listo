from fastapi import FastAPI
from database import init_db
import routes as authentication
from contextlib  import asynccontextmanager
from dotenv import load_dotenv
from strawberry.fastapi import GraphQLRouter
import strawberry
from strawberry_core import Query

@asynccontextmanager
async def lifespan(app: FastAPI):
   load_dotenv()
   await init_db()
   yield     

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI(lifespan=lifespan, root_path="/authentication")

app.include_router(graphql_app, prefix="/graphql", tags=["graphql"])
app.include_router(authentication.router, tags=["authentication"])
