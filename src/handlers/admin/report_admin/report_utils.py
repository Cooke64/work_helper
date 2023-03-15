import os
import logging

from celery_app.celery_app import create_report
from handlers.admin.report_admin import create_report_template as tmp
from pydantic_config import settings

report_func = {'html': tmp.crete_html_report,
               'txt': tmp.crete_txt_report,
               'exel': tmp.crete_hexel_report,
               }


def write_file(file_name: str, type_report: str) -> None:
    match file_name:
        case 'exel':
            pass
        case _:
            with open(file_name, 'w',  encoding='cp1251') as file:
                file_data = report_func[type_report]()
                logging.info(file_data)
                file.write(file_data)


def get_filename(type_report: str = 'html') -> str:
    file_name = f'ready_reports/report_to_send.{type_report}'
    try:
        write_file(file_name, type_report)
    except FileNotFoundError:
        local_path = 'C:\\DEV\\work_helper\\src\\handlers\\admin\\report_admin'
        docker_parh = '\\app\\handlers\\admin\\report_admin'
        os.chdir(local_path if settings.DEBUG else docker_parh)
        create_report(file_name, type_report)
    finally:
        return file_name
