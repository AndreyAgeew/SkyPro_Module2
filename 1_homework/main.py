from utils import *
from config import WORDS_PATH, HISTORY_PATH


def main() -> None:
    """
    Основная функция
    user_name (str) - передается имя пользователя
    words_of_file (list[str]) - передается запись файла в виде списка слов
    history_file (str) - передается запись файла со статистикой игр
    user_points (int) - передается кол-во очков текущего пользователя
    max_point (int) - передается максимальное кол-во очков из всех пользователей
        Functions:
            get_user_name - передает имя пользователя
            quiz - викторина (передает кол-во очков текущего пользователя)
            record_file - записывает данные в файл
            get_max_point - передает максимальное кол-во очков из всех пользователей
            output_statistics_quiz - выводит статистику игр из файла
    """
    user_name: str = get_user_name()
    words_of_file: list[str] = reading_file(WORDS_PATH).splitlines()
    user_points: int = quiz(words_of_file)
    record_file(HISTORY_PATH, f'{user_name} {user_points}\n')
    history_file: str = reading_file(HISTORY_PATH)
    max_point: int = get_max_point(history_file)
    output_statistics_quiz(history_file, max_point)


if __name__ == '__main__':
    main()
