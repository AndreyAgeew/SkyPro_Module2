from utils import get_student_by_pk, get_profession_by_title, check_fitness, output_student_result
from typing import Any


def main() -> None:
    """
    Основная функция

    student_number (int) - передается номер студента
    student (dict[str:Any]) - передается информация о студенте
    student_name (str) - передается имя студента
    profession_name (str) - передается направление профессии
    profession (dict[str:Any]) - передается информация о профессии
    student_result (dict[str:Any]) - передается соотвествие студента к профессии

        Functions:
            get_student_by_pk - вовзращает словарь с информацией о студенте
            get_profession_by_title - находит профессию по title и возвращает словарь с информацией о ней
            check_fitness - возвращает соответстве студента с выбранным направлением в профессии в виде словаря
            output_student_result - выводит результаты соответсия студента с профессией"
    """
    student_number: int = int(input("Введите номер студента: "))
    student: dict[str:Any] = get_student_by_pk(student_number)
    student_name: str = student["full_name"]
    profession_name: str = str(input(f"Выберите специальность для оценки студента {student_name}\n"))
    profession: dict[str:Any] = get_profession_by_title(profession_name)
    student_result: dict[str:Any] = check_fitness(student, profession)
    output_student_result(student_result, student_name)


if __name__ == '__main__':
    main()
