from random import choice
import requests
from classes.basic_word import BasicWord
from classes.players import Player
from typing import Any


def load_random_word(url: str) -> BasicWord:
    """Функция возвращает экземпляр класса BasicWord со случайным словом """
    random_word: dict[Any] = choice(requests.get(url).json())
    return BasicWord(random_word["word"], random_word["subwords"])


def get_player() -> Player:
    """Функция запрашивает имя игрока и вовзращает экземпляр класса Player"""
    player_name: str = input(str("Введите имя игрока: "))
    return Player(player_name)


def output_start_play(player: Player, word: BasicWord) -> None:
    """Функция выводит приветсвие и правила игры"""
    print(player)
    print(word)
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print("Поехали, ваше первое слово?")


def output_statistics(answers: int) -> None:
    """Функция выводит статистику ответов"""
    word = ''
    if answers == 1 or (answers > 20 and answers % 10 == 1) \
            and answers % 100 != 11:
        word = "слово"
    elif (answers > 1 and answers < 5) or \
            (answers > 20 and answers % 10 > 1 and answers % 10 < 5):
        word = "слова"
    elif answers == 0 or (answers > 1 and answers < 20) \
            or answers % 10 == 0 or answers % 100 >= 11 \
            or answers % 10 >= 5 or answers % 100 >= 10:
        word = "слов"
    print(f"Игра завершена, вы угадали {answers} {word}!")
