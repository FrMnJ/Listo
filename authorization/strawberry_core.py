from typing import List, Optional 
import strawberry
from strawberry_schemas import RoleType
from strawberry_controller import Queries



@strawberry.type
class Query:
    roles: List[RoleType] = strawberry.field(resolver=Queries.get_all_roles)