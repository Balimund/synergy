"""Кейс-задача № 1.

Программа запрашивает день, месяц и год рождения, определяет день недели,
високосность года, текущий возраст и выводит дату звёздочками (как на табло).
"""

from datetime import date

WEEKDAYS = [
    "понедельник", "вторник", "среда", "четверг",
    "пятница", "суббота", "воскресенье",
]

# Шрифт 5x5: каждая цифра - список из 5 строк по 5 символов
DIGITS = {
    "0": [" *** ", "*   *", "*   *", "*   *", " *** "],
    "1": ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
    "2": [" *** ", "*   *", "   * ", "  *  ", "*****"],
    "3": ["**** ", "    *", " *** ", "    *", "**** "],
    "4": ["*   *", "*   *", "*****", "    *", "    *"],
    "5": ["*****", "*    ", "**** ", "    *", "**** "],
    "6": [" *** ", "*    ", "**** ", "*   *", " *** "],
    "7": ["*****", "    *", "   * ", "  *  ", " *   "],
    "8": [" *** ", "*   *", " *** ", "*   *", " *** "],
    "9": [" *** ", "*   *", " ****", "    *", " *** "],
    " ": ["     ", "     ", "     ", "     ", "     "],
}


def get_weekday(day: int, month: int, year: int) -> str:
    """Возвращает день недели для заданной даты."""
    return WEEKDAYS[date(year, month, day).weekday()]


def is_leap_year(year: int) -> bool:
    """Возвращает True, если год високосный."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_age(day: int, month: int, year: int) -> int:
    """Возвращает количество полных лет на сегодняшний день."""
    today = date.today()
    age = today.year - year
    if (today.month, today.day) < (month, day):
        age -= 1
    return age


def render_stars(text: str) -> str:
    """Рисует строку из цифр и пробелов звёздочками."""
    lines = []
    for row in range(5):
        lines.append("  ".join(DIGITS[ch][row] for ch in text))
    return "\n".join(lines)


def ask_int(prompt: str) -> int:
    """Запрашивает целое число, повторяя запрос при ошибке ввода."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def ask_birth_date() -> tuple[int, int, int]:
    """Запрашивает дату рождения и проверяет, что она существует."""
    while True:
        day = ask_int("Введите день рождения (число): ")
        month = ask_int("Введите месяц рождения (число): ")
        year = ask_int("Введите год рождения: ")
        try:
            birth = date(year, month, day)
        except ValueError:
            print("Ошибка: такой даты не существует. Попробуйте снова.\n")
            continue
        if birth > date.today():
            print("Ошибка: дата рождения в будущем. Попробуйте снова.\n")
            continue
        return day, month, year


def main() -> None:
    day, month, year = ask_birth_date()

    print(f"\nДень недели: {get_weekday(day, month, year)}")
    print(f"Год {year} {'високосный' if is_leap_year(year) else 'не високосный'}")
    print(f"Возраст: {get_age(day, month, year)}\n")

    print(render_stars(f"{day:02d} {month:02d} {year:04d}"))


if __name__ == "__main__":
    main()
