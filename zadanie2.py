import re
from collections import Counter

def most_common_word(sentence):
    words = re.findall(r'\w+', sentence)
    word_count = Counter(words)
    return word_count.most_common(1)[0]
sentence =str(input("введите предложение : "))
most_common = most_common_word(sentence)
print(f'слово  "{most_common[0]}" было использовано {most_common[1]} раз')

#Вова пытался сделать определятор языка типо если на русском  но что то пошло не так и я не сообразил как Жаль
# print(f'слово  "{most_common[0]}" было использовано {most_common[1]} раз')
# если на англ то from langdetect import detect_langs
# for i in most_common:
#     if detect_langs(sentence) == "ru" :
#         print(f'слово  "{most_common[0]}" было использовано {most_common[1]} раз')
#     elif detect_langs(sentence) == "en":
#         print(f'word  "{most_common[0]}" repeated {most_common[1]} ')