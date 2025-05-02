import httpx


async def assign_role(user_id: int, role: str) -> bool:
    query = """
        mutation CreateUserRole($userRoleInput: UserRoleInput!) {
            createUserRole(userRoleInput: $userRoleInput) {
                id
                user
                role {
                    name
                }
            }
        }
    """
    variables = {
        "userRoleInput": {
            "userId": user_id,
            "role": role
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://authorization-service:8000/authorization/graphql",
            json={"query": query, "variables": variables},
        )
        if response.status_code == 200:
            return True
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return False