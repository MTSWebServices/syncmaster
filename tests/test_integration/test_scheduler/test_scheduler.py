import asyncio
import time

import pytest
from pytest_mock import MockType
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from syncmaster.db.models import Run, Status
from syncmaster.scheduler.transfer_fetcher import TransferFetcher
from syncmaster.scheduler.transfer_job_manager import TransferJobManager
from syncmaster.server.settings import ServerAppSettings as Settings
from tests.mocks import MockTransfer

pytestmark = [pytest.mark.asyncio, pytest.mark.worker, pytest.mark.scheduler]


async def test_scheduler(
    session: AsyncSession,
    settings: Settings,
    group_transfer_integration_mock: MockTransfer,
    transfer_job_manager: TransferJobManager,
    mock_send_task_to_tick: MockType,
    mock_add_job: MockType,
):
    group_transfer = group_transfer_integration_mock
    transfer_fetcher = TransferFetcher(settings)
    transfers = await transfer_fetcher.fetch_updated_jobs()
    assert transfers
    assert group_transfer.transfer.id in {t.id for t in transfers}

    transfer_job_manager.update_jobs(transfers)

    job = transfer_job_manager.scheduler.get_job(str(group_transfer.id))
    assert job is not None

    await asyncio.sleep(1.5)  # make sure that created job with every-second cron worked

    run = (
        await session.scalars(
            select(Run).filter_by(transfer_id=group_transfer.id).order_by(Run.created_at.desc()),
        )
    ).one()
    assert run.status in [Status.CREATED, Status.STARTED]

    started = time.perf_counter()
    while (time.perf_counter() - started) < 10:
        await asyncio.sleep(0.1)
        await session.refresh(run)
        if run.status == Status.FINISHED:
            break

    assert run.status == Status.FINISHED
    assert run.ended_at is not None
