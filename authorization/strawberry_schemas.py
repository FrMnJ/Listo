import strawberry
from typing import List, Optional

@strawberry.input
class UserRoleInput:
    user_id: int
    role: str

@strawberry.type  
class UserRoleDelete:
    id: int
    user_id: int
    role_id: int


@strawberry.type
class PermissionType:
    id: int
    name: str

@strawberry.type
class RoleWithUserRoleIdType:
    id: int
    user_role_id: int
    name: str
    permissions: List[PermissionType] = strawberry.field(default_factory=list)
@strawberry.type
class RoleType:
    id: int
    name: str
    permissions: List[PermissionType] = strawberry.field(default_factory=list)

@strawberry.type
class UserRolesOutput:
    user_id: int
    roles: List[RoleWithUserRoleIdType] = strawberry.field(default_factory=list)

@strawberry.type
class UserType:
    id: int
    username: str
    full_name: str
    email: str
    phone_number: str
    address: str
    last_login: Optional[str] = None
    is_verified: bool
    language: str
    utm_source: str
    device_used: Optional[str] = None
    location: Optional[str] = None
    url_profile: Optional[str] = None
    url_drive_license: Optional[str] = None
    url_identification: Optional[str] = None
    deleted_at: Optional[str] = None

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