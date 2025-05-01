from typing import List, Optional 
import strawberry
from strawberry_schemas import RoleType
from strawberry_controller import Queries



@strawberry.type
class Query:
    roles: List[RoleType] = strawberry.field(resolver=Queries.get_all_roles)
    get_role_by_id: Optional[RoleType] = strawberry.field(resolver=Queries.get_role_by_id)
    get_role_by_name: Optional[RoleType] = strawberry.field(resolver=Queries.get_role_by_name)
    permissions: List[RoleType] = strawberry.field(resolver=Queries.get_all_permissions)