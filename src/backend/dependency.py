

from injector import Module, singleton

from scheduler.base import BaseJob
from scheduler.sample_job import SampleJob


class Dependencies(Module):
    def configure(self, binder):

        #Bind scheduler job
        binder.bind(BaseJob, SampleJob, scope=singleton)