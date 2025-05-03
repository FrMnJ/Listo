import httpx

class AuthorizationOuput:
    def __init__(self, authorized: bool, User: dict = None):
        self.authorized = authorized
        self.User = User


async def check_authorization(token: str, action: str, object: str) -> AuthorizationOuput:
    """
    Check if the user has the required permissions to perform an action on an object.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://authorization-service:8000/authorize",
            json={
                "token": token,
                "action": action,
                "object": object,
            },
        )
        if response.status_code == 200:
            data = response.json()
            return AuthorizationOuput(
                authorized=data.get("success", False),
                User=data.get("user", None),
            )
        else:
            return AuthorizationOuput(
                authorized=False,
                User=None,
            )

