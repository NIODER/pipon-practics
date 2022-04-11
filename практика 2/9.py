russian = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф",
           "Х", "Ц", "Ч", "Ш", "Щ", "Ы", "Э", "Ю", "Я", "Ь", "Ъ"]
english = ["A", "B", "V", "G", "D", "E", "E", "ZH", "Z", "I", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U",
           "F", "KH", "TC", "CH", "SH", "SHCH", "Y", "E", "IU", "IA", "", ""]

ru_text = list(input())
en_text = []

for char in ru_text:
    if str(char).capitalize() not in russian:
        en_text.append(char)
        continue
    if str(char).isupper():
        index = russian.index(char)
        en_text.append(english[index])
    else:
        index = russian.index(char.capitalize())
        en_text.append(english[index].casefold())

print("".join(en_text))