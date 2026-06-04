enlet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
rulet = [chr(i) for i in range(ord("а"), ord("я") + 1)]


def inputdata():
    global cipr, lang, text, lenght
    cipr = int(input("Введите: '1'- Зашифровать '2'- Дешифровать "))
    while cipr != 1 and cipr != 2:
        cipr = int(input("Попробуйте снова: '1'- Зашифровать '2'- Дешифровать "))
    lang = input("Введите язык: ру или en ")
    while lang != "en" and lang != "ру":
        lang = input("Попробуйте снова: ру или en ")
    if lang == "en":
        lang = enlet
    elif lang == "ру":
        lang = rulet
    text = input("Ведите текст на выбранном языке ")
    lenght = int(input("Введите дистанцию шифра: натуральное число "))
    while lenght < 1:
        lenght = int(input("Попробуйте снова: натуральное число "))


inputdata()


while lenght > len(lang):
    lenght -= len(lang)


def cipher(language, cipher):
    resulte = []
    for lenght in range(26):
        if cipher == 1:
            for i in text.lower():
                if i.isalnum() == False:
                    resulte += i
                elif language.index(i) + lenght > (len(language) - 1):
                    resulte += language[language.index(i) + lenght - (len(language))]
                else:
                    resulte += language[language.index(i) + lenght]
        elif cipher == 2:
            for i in text.lower():
                if i.isalnum() == False:
                    resulte += i
                elif language.index(i) - lenght < 0:
                    resulte += language[language.index(i) - lenght + (len(language))]
                else:
                    resulte += language[language.index(i) - lenght]
        cip = "".join(resulte)
    return cip


cipher = cipher(lang, cipr)


def registerup():
    global cipher
    cipher = list(cipher)
    for i in range(len(text)):
        if text[i].isupper():
            cipher[i] = cipher[i].upper()
    cipher = "".join(cipher)
    return cipher


print(registerup())
