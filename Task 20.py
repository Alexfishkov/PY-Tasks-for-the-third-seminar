# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

import os
n = 0
dictionary = {}
dictionary = \
    {
        '1': 'AEIOULNSTRАВЕИНОРСТ',
        '2': 'DGДКЛМПУ',
        '3': 'BCMPБГЁЬЯ',
        '4': 'FHVWYЙЫ',
        '5': 'KЖЗХЦЧ',
        '8': 'JXШЭЮ',
        '10': 'QZФЩЪ'
    }

os.system('CLS')
yourWord = input("Введите ваше слово (на английском или русском языке)=> ")
for i in yourWord:
    for k in dictionary.keys():
        if (i.upper() in dictionary[k]):
            n +=int(k)
print(f"Стоимость вашего слова: {n}")
    
