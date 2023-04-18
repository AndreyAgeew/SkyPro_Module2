from random import sample


def record_file(file_name: str, record: str):
    """
    Функция открытия файла и записи в него (автоматическое закрытие файла)
    :param file_name: имя файла
    :type: str
    :param record: значение, которое будет записано в файл
    :type: str
    """
    with open(file_name, 'a', encoding='utf-8') as file_write:
        file_write.write(record)


def reading_file(file_name: str):
    """
        Функция открытия файла и чтение его (автоматическое закрытие файла)
        :param file_name: имя файла
        :type: str
        :return: file_read - возвращает запись из файла
        """
    with open(file_name, 'r', encoding='utf-8') as file_read:
        return file_read.read()


def get_user_name() -> str:
    """Функция получает и передает имя пользователя"""
    return str(input('Введите ваше имя: '))


def quiz(words_for_file: list[str]) -> int:
    """
    Функция викторина (кол-во очков за угаданные ответы пользователем)
    :param words_for_file: список слов из файла
    :type: list[str]
    points (int) - кол-во очков пользователя за отгаданные ответы (по default 0)
    :return: points
    """
    points: int = 0
    for word in words_for_file:
        print(f'Угадайте слово: {"".join(sample(word, len(word)))}')
        if word.lower() == str(input('')).lower():
            print('Верно! Вы получаете 10 очков.\n')
            points += 10
        else:
            print(f'Неверно! Верный ответ {word}.\n')
    return points


def get_max_point(file: str) -> int:
    """
    Функция передает максимальное кол-во очков из пользователей
    :param file: файл с результатами игр
    :type: str
    :return: максимальное кол-во очков из пользователей
    """
    return max([int(line.split()[-1]) for line in file.splitlines()])


def output_statistics_quiz(file: str, max_point: int) -> None:
    """
    Функция выводит статистику викторины
    :param file: файл с результатами игр
    :type: str
    :param max_point: максимальное кол-во очков из пользователей
    :type: int
    """
    print(f'{file}\n'
          f'Всего игр сыграно: {len(file.splitlines())}\n'
          f'Максимальный рекорд: {max_point}')
