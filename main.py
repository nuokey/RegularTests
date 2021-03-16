import re

text = '''Привет. Я пишу этот текст для того, чтобы его проверили на наличие различных символов регулярными выражениями. Я. Круто. Надеюсь, все будет нормально. Передаю числа: 123 42564256 4562456 7654 12 4324 23  34234 56546   566 56 55 '''

all_numbers = re.compile(r'\d+')
numbers_2 = re.compile(r'\s\d{2}\s')
main_chars = re.compile(r'\b[А-ЯЁ][а-яё]*?\b')
words_to_dot = re.compile(r'\b[А-ЯЁ, а-яё][а-яё]*?\b\.')

print('Все числа: ' + str(all_numbers.findall(text)))

print('Двузначные числа: ' + str(numbers_2.findall(text)))

print('Слова с заглавными буквами: ' + str(main_chars.findall(text)))

print('Слова перед точкой: ' + str(words_to_dot.findall(text)))