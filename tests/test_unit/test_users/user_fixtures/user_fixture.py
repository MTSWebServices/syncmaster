from collections.abc import Callable

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from tests.mocks import MockUser, UserTestRoles
from tests.test_unit.conftest import add_user_to_group
from tests.test_unit.utils import create_group, create_user


@pytest_asyncio.fixture
async def superuser(session: AsyncSession, access_token_factory) -> MockUser:
    user = await create_user(session, username="superuser", is_superuser=True)
    return MockUser(
        user=user,
        auth_token=access_token_factory(user.id),
        role=UserTestRoles.Superuser,
    )


@pytest_asyncio.fixture
async def simple_user(session: AsyncSession, access_token_factory) -> MockUser:
    user = await create_user(session, username="simple_user")
    return MockUser(
        user=user,
        auth_token=access_token_factory(user.id),
        role=UserTestRoles.Developer,
    )


@pytest_asyncio.fixture(params=[5])
async def simple_users(
    request: pytest.FixtureRequest,
    session: AsyncSession,
    access_token_factory: Callable[[int], str],
) -> list[MockUser]:
    size = request.param
    users = []
    for i in range(size):
        username = f"simple_user_{i}"
        user = await create_user(
            session=session,
            username=username,
            email=f"{username}@user.user",
            first_name=f"{username}_first",
            middle_name=f"{username}_middle",
            last_name=f"{username}_last",
            is_superuser=False,
        )
        token = access_token_factory(user.id)
        mock_user = MockUser(
            user=user,
            auth_token=token,
            role=UserTestRoles.Developer,
        )
        users.append(mock_user)

    return users


@pytest_asyncio.fixture
async def user_with_many_roles(
    session: AsyncSession,
    simple_user: MockUser,
    access_token_factory: Callable[[int], str],
) -> MockUser:
    user = await create_user(
        session=session,
        username="multi_role_user",
    )

    roles = [
        UserTestRoles.Owner,
        UserTestRoles.Maintainer,
        UserTestRoles.Developer,
        UserTestRoles.Guest,
    ]

    groups = []

    for role in roles:
        group = await create_group(
            session=session,
            name=f"group_for_{role}",
            owner_id=user.id if role == UserTestRoles.Owner else simple_user.user.id,
        )

        if role != UserTestRoles.Owner:
            await add_user_to_group(user=user, group_id=group.id, session=session, role=role)
        groups.append(group)

    token = access_token_factory(user.id)
    mock_user = MockUser(
        user=user,
        auth_token=token,
    )

    return mock_user
