from unittest.mock import AsyncMock

import pytest

from handlers.users.start import run_start_command, get_main_buttons
from messages.message_text import HELLO_TEXT


@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    await run_start_command(message)
    message.answer.assert_called_with(
        f'Привет, {message.from_user.full_name}.\n{HELLO_TEXT}',
        reply_markup=get_main_buttons(message.from_user.id)
    )
