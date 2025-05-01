import strawberry
from typing import List, Optional

@strawberry.type
class PermissionType:
    id: int
    name: str

@strawberry.type
class RoleType:
    id: int
    name: str
    permissions: List[PermissionType] = strawberry.field(default_factory=list)

@strawberry.type
class UserRoleType:
    id: int
    user: int
    role: RoleType

@strawberry.type
class RolePermissionType:
    id: int
    role: RoleType
    permission: PermissionType