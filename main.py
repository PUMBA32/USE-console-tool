import os
import sys

import matplotlib.pyplot as plt

from datetime import datetime
from typing import Optional, Union


'''
Информатика - 27 заданий
Профильная математика - 12 заданий
Русский язык - 26 заданий
'''

def cls() -> None:
    os.system("cls" if sys.platform == 'win32' else 'clear')


class Constants:
    BASE_PATH: str = os.path.dirname(__file__)
    DATA_PATH: str = os.path.join(BASE_PATH, 'data')
    
    IT_FOLDER: str = os.path.join(DATA_PATH, 'информатика')
    MATH_FOLDER: str = os.path.join(DATA_PATH, 'математика')
    RUS_FOLDER: str = os.path.join(DATA_PATH, 'русский язык')

    IT_DATA: str = os.path.join(IT_FOLDER, 'информатика.txt')
    MATH_DATA: str = os.path.join(MATH_FOLDER, 'математика.txt')
    RUS_DATA: str = os.path.join(RUS_FOLDER, 'русский язык.txt')


class Diagram:
    @staticmethod
    def diagram(data: list[str], optional_params: Optional[str] = None) -> None: 
        print(optional_params)


class FileWorker:
    @staticmethod
    def get_lines(path: str) -> Optional[list]:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return file.readlines()
        except Exception as e:
            cls()
            print(f'Ошибка получения данных! {e}\n')
            return 
        
    
    @staticmethod
    def delete_row(path: str, index: int) -> Optional[list]:
        cls()
        try:
            with open(path, 'r', encoding='utf-8') as file:
                lines: list = file.readlines()

            length: int = len(lines)

            if index > length or index < 0:
                print("Ошибка! некорректный номер строки\n")
                return

            with open(path, 'w', encoding='utf-8') as file:
                for i in range(length):
                    if i != index-1:
                        file.write(lines[i])
        except Exception as e:
            print(f'Ошибка получения данных! {e}\n')
            return 
        else:
            print("Запись успешно удалена!\n")

    
    @staticmethod
    def write(path: str, row: str) -> None:
        cls()
        try:
            with open(path, 'a', encoding='utf-8') as file:
                file.write(row)
        except Exception as e:
            print(f'Ошибка записи данных! {e}\n')
            return 
        else:
            print('Данные успешно сохранены!\n')
        

    @staticmethod
    def create_empty(path: str) -> Optional[list]:
        try:
            with open(path, 'w', encoding='utf-8') as _: ...
        except Exception as e:
            cls()
            print(f'Ошибка создания папки! {e}\n')
            return 
        
    
    @staticmethod
    def show_file_content(data: list) -> None:
        cls()
        if len(data) > 0:
            for i, row in enumerate(data):
                print(f"{i+1}. {row}", end="")
            print()
        else:
            print("тут ничего нет...\n")
        

class Program: 
    def __init__(self) -> None: 
        self._menu: list = [
            'Добавить пробник',
            'Удалить пробник',
            'Статистика по предметам',
            'Выход'
        ]

        cls()
        self.__check()

    
    def __check(self) -> None:
        os.makedirs(Constants.IT_FOLDER, exist_ok=True)
        os.makedirs(Constants.MATH_FOLDER, exist_ok=True)
        os.makedirs(Constants.RUS_FOLDER, exist_ok=True)

        for p in (Constants.IT_DATA, Constants.MATH_DATA, Constants.RUS_DATA):
            if not os.path.exists(p):
                FileWorker.create_empty(p)
                print(f"[log] file {p} was created.")
        print()
   

    def show_menu(self) -> None:
        for i, el in enumerate(self._menu):
            print(f"[{i+1}] - {el}")
        print()


    def run(self) -> None: 
        while 1:
            self.show_menu()
            choice: str = input(">>> ").strip()

            match choice:
                case "1": self.add()
                case "2": self.delete()
                case "3": self.stats()    
                case _: return


    def __path(self) -> Optional[str]:
        cls()
        print("Enter 'q' for go back.")
        print("[1] Информатика\n[2] Математика\n[3] Русский язык\n")
        choice: str = input(">>> ").strip()

        match choice:
            case "1": return Constants.IT_DATA
            case "2": return Constants.MATH_DATA
            case "3": return Constants.RUS_DATA
            case _: 
                cls()
                return 


    def add(self) -> None:
        # получаем путь до файла с данными по вводу пользователя и проверяем является ли полученный путь None
        if (path := self.__path()) == None: return  

        # данные сохраняются в формате: дата, количество решенных заданий
        try:
            count: int = int(input("Количество верно решенных заданий: ").strip())  # количество решенных заданий
        except ValueError as e:
            cls()
            print(f"Ошибка, вы должны ввести число!\n")
            return
        else:
            row: str = f'{datetime.now().date().strftime("%d/%m/%Y")} {count}\n'
            FileWorker.write(path, row)

    
    def delete(self) -> None:
        # получаем путь до файла с данными по вводу пользователя и проверяем является ли полученный путь None
        if (path := self.__path()) == None: return 

        # получаем содержимое файла и выводим его на экран
        file_content: list[str] = FileWorker.get_lines(path)
        FileWorker.show_file_content(file_content)

        if len(file_content) > 0:  # если в файле есть какие то данные
            try:
                index: int = int(input("Номер записи для удаления: ").strip())
            except ValueError:
                cls()
                print(f"Ошибка, вы должны ввести число!\n")
                return
            else:
                FileWorker.delete_row(path, index)

    
    def stats(self) -> None: 
        # получаем путь до файла с данными по вводу пользователя и проверяем является ли полученный путь None
        if (path := self.__path()) == None: return 
        
        # получаем содержимое файла и выводим его на экран
        file_content: list[str] = FileWorker.get_lines(path)
        FileWorker.show_file_content(file_content)

        if len(file_content) > 0:
            scores: list[int] = [int(line.split(" ")[1].replace("\n", '')) for line in file_content]
            
            count: int = len(scores)
            max_score: int = max(scores)
            min_score: int = min(scores)
            mid: float = round(sum(scores)/len(scores), 2)
            mid_by_last_values: Union[float, str] = round((scores[-1]+scores[-2]+scores[-3])/count, 2) if count >= 3 else "too less values"

            optional_params: str = f'count of values: {count}\nmax score: {max_score}\nmin score: {min_score}\nmiddle grade: {mid}\nmiddle grade by last 3 values: {mid_by_last_values}'
            Diagram.diagram(file_content, optional_params)

    
def main() -> None: 
    program = Program()
    program.run()


if __name__ == '__main__':
    main()

