import os

from config import DEBUG
from handlers.admin.report_admin import create_report_template as tmp

report_func = {'html': tmp.crete_html_report,
               'txt': tmp.crete_txt_report,
               'exel': tmp.crete_hexel_report,
               }


def write_file(file_name: str, type_report: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        file_data = report_func[type_report]()
        file.write(file_data)


def get_filename(type_report: str = 'html') -> str:
    file_name = f'ready_reports/report_to_send.{type_report}'
    try:
        write_file(file_name, type_report)
    except FileNotFoundError:
        local_path = 'C:\\DEV\\work_helper\\src\\handlers\\admin\\report_admin'
        docker_parh = ''
        os.chdir(local_path if DEBUG else docker_parh)
        write_file(file_name, type_report)
    finally:
        return file_name
