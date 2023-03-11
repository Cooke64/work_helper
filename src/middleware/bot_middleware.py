from typing import Callable, Dict, Any, Awaitable

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types.base import TelegramObject


class BotMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[
                [TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        # before
        print(event)
        result = await handler(event, data)
        # after
        return result

    async def pre_process(self, obj, data, *args):
        print(obj)

    async def post_process(self, obj, data, *args):
        pass
