class Player:
    """
    Базовыый класс Player
        Args:
            name (str) - передается имя пользователя
        Attributes:
            __used_subwords (list[str]) - передается испольвазонные ответы
    """

    def __init__(self, name: str):
        self.name: str = name
        self.__used_subwords: list[str] = []

    @property
    def name(self) -> str:
        """Геттер для имени игрока"""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Сеттер для имени игрока"""
        while True:
            if value == " ".join([item for item in value.split() if item.isalpha()]):
                self.__name = value.title()
                break
            else:
                value = str(input("Введите корректное имя пользователя: "))

    @property
    def get_amount_used_subwords(self) -> int:
        """Метод возвращает кол-во использованных слов"""
        return len(self.__used_subwords)

    def append_subword_in_used_subwords(self, sub_word: str) -> None:
        """Метод добавляет подслово в список использованных подслов"""
        self.__used_subwords.append(sub_word)

    def is_subword_in_used_subwords(self, sub_word: str) -> bool:
        """Метод возвращает True или False в зависимости есть ли подслово в списке использованных подслов"""
        return sub_word in self.__used_subwords

    def __repr__(self) -> str:
        """Метод возвращает привествие пользователя."""
        return f"Привет, {self.name}!"
