from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InputFile

from handlers.admin.report_admin.report_utils import get_filename
from keayboards.inline_buttons import ADMIN_REPORT_KB
from loader import dp, bot
from states.admin_report_state import AdminReportState


@dp.message_handler(lambda mes: mes.text in 'Скачать отчет.')
async def start_createng_report(message: types.Message):
    await message.answer(
        'Выбери в каком формате хочшеь получить отчет.\n',
        reply_markup=ADMIN_REPORT_KB
    )
    await AdminReportState.type_report.set()


@dp.callback_query_handler(text=['txt', 'html', 'exel'],
                           state=AdminReportState.type_report)
async def send_report(call: CallbackQuery, state: FSMContext):
    await state.update_data(ready_to_start=call.data)
    await call.message.answer(f'Выбрали формат {call.data} для отчета.')
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    file = InputFile(get_filename(call.data))
    await call.message.answer_document(file)
    await state.finish()
