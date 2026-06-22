import pytest

from .users_repository import UsersRepository


@pytest.mark.asyncio
@pytest.mark.skip(reason="Insert in DB")
async def test_insert_user():
    new_user = {"user_name": "NomeDeTeste", "age": 99, "uf": "SP"}
    repo = UsersRepository()
    await repo.insert_users(new_user)


@pytest.mark.skip(reason="Insert in DB")
@pytest.mark.asyncio
async def test_get_users_by_name():
    repo = UsersRepository()
    response = await repo.get_users_by_name("fulano")
    print(response)
