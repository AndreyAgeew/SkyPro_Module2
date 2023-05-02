class Question:
    """
    Базовый класс вопросы
        Args:
            __question_text - передается текст вопроса
            __question_level - передается сложность вопроса
            __correct_answer -  передается правлиьный ответ на вопрос

        Attributes:
            __is_answer - передается есть ли вопрос (bool)
            user_answer - передается ответ на вопрос от пользователя
            __points - передается очки за вопрос
    """

    def __init__(self, question_text: str, question_level: str, correct_answer: str):
        self.__question_text: str = question_text
        self.__question_level: str = question_level
        self.__correct_answer: str = correct_answer

        self.__is_answer: bool = False
        self.user_answer = None
        self.__points: int = self.points

    @property
    def user_answer(self):
        """Геттер для ответа пользователя"""
        return self.user_answer

    @user_answer.setter
    def user_answer(self, value):
        """Cеттер для ответа пользователя"""
        self.__user_answer = value

    @property
    def points(self):
        """Возвращает int, количество баллов.
                Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return int(self.__question_level) * 10

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
                с верным ответов иначе False.
        """
        return self.__correct_answer == self.__user_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
                Вопрос: What do people often call American flag?
                Сложность 4/5
        """
        return f"Вопрос: {self.__question_text}\nСложность: {self.__question_level}/5"

    def build_feedback(self):
        """Возвращает :
                Ответ верный, получено __ баллов
                            или
                Ответ неверный, верный ответ __
        """
        feedback = f"Ответ верный, получено {self.__points} баллов" if self.is_correct() \
            else f"Ответ неверный, верный ответ {self.__correct_answer}"
        return feedback
