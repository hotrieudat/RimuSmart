

from abc import ABC, abstractmethod


class BaseJob(ABC):
    @abstractmethod
    async def execute(self):
        """Logic chính của Job sẽ nằm ở đây"""
        pass

    async def run_with_scope(self):
        """Hàm bao đóng để quản lý RequestScope và lỗi"""
        # factory = injector.get(RequestScopeFactory)
        # async with factory.create_scope():
        try:
            await self.execute()
        except Exception as e:
            # Log lỗi cụ thể tại đây
            print(f"Error in {self.__class__.__name__}: {e}")

