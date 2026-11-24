import secrets
from collections.abc import Callable

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from syncmaster.db.models import Group
from tests.mocks import MockUser, UserTestRoles
from tests.test_unit.utils import create_group, create_queue, create_user


@pytest_asyncio.fixture
async def group_owner(
    session: AsyncSession,
    access_token_factory: Callable[[int], str],
):
    user = await create_user(
        session=session,
        username=secrets.token_hex(5),
    )

    token = access_token_factory(user.id)
    return MockUser(
        user=user,
        auth_token=token,
        role=UserTestRoles.Owner,
    )


@pytest_asyncio.fixture
async def group(
    session: AsyncSession,
    group_owner: MockUser,
):
    result = await create_group(session=session, name=secrets.token_hex(5), owner_id=group_owner.user.id)
    return result


@pytest_asyncio.fixture(params=["123-test_queue"])
async def queue(
    request: pytest.FixtureRequest,
    session: AsyncSession,
    group: Group,
):
    result = await create_queue(
        session=session,
        name=request.param,
        group_id=group.id,
        slug=request.param,
    )
    return result
