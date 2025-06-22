# ДЗ от 01.06.2025
# 1. Получить текст от пользователя: Программа должна запросить у пользователя ввод строки текста.
# #
# 2. Подсчитать количество гласных и согласных букв:
# Определите, какие буквы считаются гласными
# (например, "а", "е", "и", "о", "у", "ы", "э", "ю", "я" в русском языке,
# а также их заглавные эквиваленты).
# Все остальные буквы алфавита считаются согласными.
# Учитывайте только буквы русского алфавита, игнорируйте цифры, знаки препинания и пробелы.
#
# 3. Найти самое длинное слово:
# Разделите текст на слова.
# Определите слово с наибольшей длиной.
# Если есть несколько слов одинаковой максимальной длины, выведите любое из них.
#
# 4. Подсчитать количество вхождений заданного слова:
# Программа должна запросить у пользователя слово для поиска.
# Подсчитайте, сколько раз это слово встречается в тексте (без учета регистра).

string = input("Введите текст: ")
search_word = input("Введите слово для поиска: ")
text = string.upper()

vowels = "АОУЫИЭЕЁЮЯ"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Количество гласных букв:", vowel_count)
print("Количество согласных букв:", consonant_count)

words = string.split()
max_word = ""
for word in words:
    clean_word = ""
    for char in word:
        if char.isalpha():
            clean_word += char
# сокращенный вариант вложенного цикла:
    clean_word = "".join([c for c in word if c.isalpha()])
    if len(clean_word) > len(max_word):
        max_word = clean_word

print("Самое длинное слово:", max_word)


normalized_words = []
for word in words:
    clean = "".join([c for c in word if c.isalpha()])
    normalized_words.append(clean)

print("Количество вхождений слова:", normalized_words.count(search_word))