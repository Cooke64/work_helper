from typing import Any

import jinja2

from database import admin_crud as crud
from database.user_model import UserMessage

environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates/')
)


def get_users_data() -> tuple[
    list[UserMessage] | bool,
    [UserMessage],
    [UserMessage]
]:
    user_passed_test = crud.get_passed_test()
    all_users = crud.get_all_users()
    users_with_phones = crud.get_user_with_phones()
    return user_passed_test, all_users, users_with_phones


def get_data_dict() -> dict[list[UserMessage], list[UserMessage] | bool | Any]:
    passed, all_users, with_phone = get_users_data()
    data = {
        'passed': passed,
        'all_users': all_users,
        'with_phone': with_phone
    }
    return data


def render_to_template(template: str, content: dict, ):
    template = environment.get_template(template)
    return template.render(content)


def crete_html_report():
    return render_to_template('report.html', content=get_data_dict())


def crete_txt_report():
    return render_to_template('report.txt', content=get_data_dict())


def crete_hexel_report():
    return render_to_template('report.xml', content=get_data_dict())
