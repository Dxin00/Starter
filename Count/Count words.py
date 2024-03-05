import string

text = input("Введите текст: ")

# Подсчет слов
words = text.split()
word_count = len(words)

# Подсчет символов
letter_count = len(text)

# Подсчет пробелов
space_count = text.count(" ")

# Подсчет специальных символов
special_char_count = sum(text.count(char) for char in string.punctuation)

# Подсчет символов без пробелов и специальных символов
cleaned_text = text.translate(str.maketrans('', '', string.punctuation + ' '))
char_count_without_spaces_and_punctuation = len(cleaned_text) - space_count

# Подсчет абзацев
paragraph_count = len([p for p in text.split('\n') if p.strip() != ''])

print(f"Слов: {word_count}")
print(f"Знаков: {letter_count}")
print(f"Специальные символы: {special_char_count}")
print(f"Пробелов: {space_count}")
print(f"Символов без пробелов и пунктуации: {char_count_without_spaces_and_punctuation}")
print(f"Абзацы: {paragraph_count}")
input()