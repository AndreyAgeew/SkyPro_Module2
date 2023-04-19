from config import WORDS_URL_JSON
from utils import *


def main() -> None:
    """
    Основная функция
    player - экзмпляр класса Player
    basic_word - экземпляр класса BasicWord
    user_subword - передается подслово, которое ввел пользователь
        Functions and methods:
            output_start_play (function) - выводит приветсвие и правила игры
            get_amount_used_subwords (method) - метод класса Player, возвращает кол-во использованных подслов
            get_amount_subwords (method) - метод класса BasicWord, возвращает кол-во подслов слова
            get_min_length_subword (method) - метод класса BasicWord, возвращает самую минимальную длину из подслов
            is_user_subword_in_subwords (method) - метод класса BasicWord, возвращает есть ли подслово,
                                                 которое ввел пользователь в списке подслов
            is_subword_in_used_subwords (method) - метод класса Player, проверяет есть ли подслово
                                                в списке использованных подслов
            append_subword_in_used_subwords (method) - метод класса BasicWord, добавляет подслово в
                                                        список использованных подслов
            output_statistics (function) - выводит статистику игры

    """
    player: Player = get_player()
    basic_word: BasicWord = load_random_word(WORDS_URL_JSON)
    output_start_play(player, basic_word)
    while player.get_amount_used_subwords < basic_word.get_amount_subwords:
        user_subword = str(input()).lower()
        if user_subword.lower() in ['stop', 'стоп']:
            break
        else:
            if len(user_subword) < basic_word.get_min_length_subword:
                print("слишком короткое слово")
            elif not basic_word.is_user_subword_in_subwords(user_subword):
                print("неверно")
            elif player.is_subword_in_used_subwords(user_subword):
                print("уже использовано")
            else:
                print("верно")
                player.append_subword_in_used_subwords(user_subword)
    output_statistics(player.get_amount_used_subwords)


main()
