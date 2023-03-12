import logging

from handlers.admin.report_admin import create_report_template as tmp

report_func = {'html': tmp.crete_html_report,
               'txt': tmp.crete_txt_report,
               'exel': tmp.crete_hexel_report,
               }


def get_filename(type_report: str = 'html') -> str:
    file_name = f'reports/report_to_send.{type_report}'
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file_data = report_func[type_report]()
            file.write(file_data)
    except FileNotFoundError:
        logging.error('не найден файл')
    finally:
        return file_name
