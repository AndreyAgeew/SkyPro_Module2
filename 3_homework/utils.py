import requests
from random import shuffle
from classes.question import Question


def _load_json_url(url: str) -> list[dict[str:str]]:
    """Служебная функция для загрзуки json с url"""
    return requests.get(url).json()


def get_player_questions(url: str):
    """Возвращает список вопросов"""
    questions_shuffle: list[dict[str:str]] = _load_json_url(url)
    shuffle(questions_shuffle)
    player_questions: list[Question] = []
    for question in questions_shuffle:
        player_questions.append(Question(question["q"], question["d"], question["a"]))
    return player_questions


def get_result_game(questions: list[Question]):
    """Возвращает результат игры (кол-во правильнх ответов, кол-во баллов за игру)"""
    amount_corrcet_answers: int = 0
    amount_points: int = 0
    for question in questions:
        if question.is_correct():
            amount_points += question.points
            amount_corrcet_answers += 1
    return amount_corrcet_answers, amount_points


def output_result_game(amount_points: int, amount_correct_answers: int):
    """Выводит результат игры"""
    print('\nВот и всё!')
    print(f'Отвечено {amount_correct_answers} вопроса из 5')
    print(f'Набрано баллов: {amount_points}')
