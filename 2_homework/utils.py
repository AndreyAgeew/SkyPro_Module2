import os
import json
from typing import Any


def read_file(path):
    """Функция для чтения json файла"""
    with open(path, 'r') as fp:
        return json.load(fp)


def load_students() -> list[dict]:
    """Функция вовзращает список с информацией о студентах"""
    path = os.path.abspath("data/students.json")
    return read_file(path)


def load_professions() -> list[dict]:
    """Функция вовзращает список с информацией о профессиях"""
    path = os.path.abspath("data/professions.json")
    return read_file(path)


def get_student_by_pk(pk: int) -> dict[str:Any]:
    """
    Функция вовзращает словарь с информацией о студенте
    :param pk:  передает номер студента
    :type: int
    :return: словарь с информацией о студенте
    """
    students: list[dict] = load_students()
    if pk <= 0 or pk > len(students):
        print("У нас нет такого студента")
        exit()
    student: dict = students[pk - 1]
    print(f"Студент {student['full_name']}")
    print(f"Знает {', '.join(student['skills'])}")
    return student


def get_profession_by_title(title: str) -> dict[str:Any]:
    """
    Функция находит профессию по title и возвращает словарь с информацией о ней
    :param title: название профессии
    :return: словарь с информацией о профессии
    """
    professions: list[dict] = load_professions()
    for profession in professions:
        if profession["title"] == title.title():
            return profession
    print("У нас нет такой специальности")
    exit()


def check_fitness(student: dict[str:Any], proffesion: dict[str:Any]) -> dict[str:Any]:
    """Функция возвращает соответстве студента с выбранным направлением в профессии в виде словаря"""
    has_skill: set = set(student["skills"]).intersection(proffesion["skills"])
    lacks: set = set(proffesion["skills"]).difference(student["skills"])
    fit_percent: int = round(100 / len(proffesion["skills"]) * len(has_skill))
    return {"has_skill": has_skill, "lacks": lacks, "fit_percent": fit_percent}


def output_student_result(result, student_name) -> None:
    """Функция выводит результаты соответсия студента с профессией"""
    print(f"Пригодность {result['fit_percent']}%")
    print(f"{student_name} знает {', '.join(result['has_skill'])}")
    print(f"{student_name} не знает {', '.join(result['lacks'])}")
