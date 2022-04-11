def month_name(number, language):
    months_en = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december"
    ]
    months_ru = [
        "январь",
        "февраль",
        "март",
        "апрель",
        "май",
        "июнь",
        "июль",
        "август",
        "сентябрь",
        "октябрь",
        "ноябрь",
        "декабрь"
    ]

    if language == "en":
        return months_en[int(number) - 1]
    elif language == "ru":
        return months_ru[int(number) - 1]
    else:
        return ""


print(month_name(3, "en"))

