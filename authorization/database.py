import os
from tortoise import Tortoise
from roles_permissions_seeder import seed_roles_permissions

async def init_db():
    host = os.environ.get("POSTGRES_HOST", "localhost")
    port = os.environ.get("POSTGRES_PORT", "5432")
    user = os.environ.get("POSTGRES_USER", "postgres")
    password = os.environ.get("POSTGRES_PASSWORD", "password")
    db = os.environ.get("POSTGRES_DB", "postgres")
    db_url = f"postgres://{user}:{password}@{host}:{port}/{db}"
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()
    await seed_roles_permissions()