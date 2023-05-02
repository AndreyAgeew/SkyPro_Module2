from utils import get_player_questions, get_result_game, output_result_game
from config import QUESTIONS_URL_JSON
from classes.question import Question


def main() -> None:
    """
    Оснвоная функция
    player_questions_list - передается список вопросов
    amount_corrcet_answers - передается кол-во правильно отвеченных вопросв
    amount_points - передется кол-во очков набранных за игру
    output_result_game - выводит результат игры
    """
    player_questions_list: list[Question] = get_player_questions(QUESTIONS_URL_JSON)
    for question in player_questions_list:
        print(question.build_question())
        question.user_answer = input()
        print(question.build_feedback())
    amount_corrcet_answers, amount_points = get_result_game(player_questions_list)
    output_result_game(amount_points, amount_corrcet_answers)


if __name__ == '__main__':
    main()
