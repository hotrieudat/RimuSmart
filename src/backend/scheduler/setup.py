from injector import Injector
from fastapi_injector.request_scope import RequestScope, RequestScopeFactory, RequestScopeOptions
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scheduler.sample_job import SampleJob
from scheduler.base import BaseJob

def setup_scheduler(injector: Injector, options: RequestScopeOptions = RequestScopeOptions()):
    scheduler = AsyncIOScheduler()
    scope_instance = injector.get(RequestScope)
    scope_instance.options = options

    # Hàm wrapper để lấy job từ injector mỗi khi chạy
    async def job_wrapper(job_class):
        factory = injector.get(RequestScopeFactory)
        async with factory.create_scope():
            # Lấy instance của Job từ injector (để nó tự bơm MyService, Logger vào)
            job_instance: BaseJob = injector.get(job_class)
            await job_instance.run_with_scope()

    # Đăng ký các Job
    scheduler.add_job(job_wrapper, 'interval', seconds=5, args=[SampleJob])
    # scheduler.add_job(job_wrapper, 'cron', hour=0, args=[OtherJob])

    scheduler.start()
    return scheduler