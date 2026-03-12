

from injector import inject
from scheduler.base import BaseJob
import asyncio

@inject
class SampleJob(BaseJob):
    def __init__(self):
        pass

    async def execute(self):
        await asyncio.sleep(1)  # Simulate some async work
        print(f"Sync completed for SampleJob")