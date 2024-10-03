import random

answers = ['да', "нет", "Бесспорно", 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено']
print('Привет я магический шар, как тебя зовут?')
name = input()
print(f"Привет, {name}")
while True:
    ask = input('Задай вопрос!')
    print(random.choice(answers))
    want = input('Дальше?')
    if want.lower() == 'нет':
        break
