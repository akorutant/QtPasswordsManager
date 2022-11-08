import csv
from database.database import DataBase


# Класс для экспорта паролей
class Exporter:
    def __init__(self,
                 file_name: str,
                 login: str
                 ):
        self.file_name = file_name
        self.login = login
        self.database = DataBase('./users.sqlite')

    # Функция для экспорта паролей в csv файл.
    def export_to_csv(self):
        try:
            data = self.database.select_all_passwords(self.login)
            headers = [(i[1] for i in self.database.select_headers()[1:-1])]
            # Если в базе есть данные, то они будут экспортированы.
            if data:
                with open(self.file_name, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                    for i in headers:
                        writer.writerow(i)
                    for i in data:
                        writer.writerow(i)
                    return True
            return False
        except Exception as error:
            return error
