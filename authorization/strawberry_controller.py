from typing import List
from models import Role
from strawberry_schemas import RoleType


class Queries:
    async def get_all_roles(self) -> List[RoleType]:
        """
        Fetch all roles from the database.
        """
        roles = await Role.all()
        return [RoleType(id=role.id, name=role.name) for role in roles]