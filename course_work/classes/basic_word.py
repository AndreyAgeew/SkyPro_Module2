class BasicWord:
    """
    Базовый класс BasicWord
        Args:
            word (str) - передается слово
            sub_words (list[str]) - передается список подслов
    """

    def __init__(self, word: str, sub_words: list[str]) -> None:
        self.__word = word
        self.__sub_words = sub_words

    def is_user_subword_in_subwords(self, user_subword) -> bool:
        """Метод возвращает есть ли подслово, которое ввел пользователь в списке подслов"""
        return user_subword in self.__sub_words

    @property
    def get_amount_subwords(self) -> int:
        """Метод возвращает кол-во подслов слова"""
        return len(self.__sub_words)

    @property
    def get_min_length_subword(self):
        """Метод возвращает самую минимальную длину из подслов"""
        return len(min(self.__sub_words, key=len))

    def __repr__(self):
        """Метод вовзращает информацию о слове и кол-ве его подслов"""
        return f"Составьте {self.get_amount_subwords} слов из слова {self.__word.upper()}" \
               f"\nСлова не должны быть короче {len(min(self.__sub_words, key=len))}-х букв"
