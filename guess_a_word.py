import random


def intro():
    """Функция входа в игру. Формируется вопрос и шаблон ответа."""
    question = {
        'жупа': 'Как у западных и южных славян назывались селение, деревня, курень?',
        'сковорода': 'Что использовали в Китае для глажки белья вместо утюга?',
        'буревестник': 'В словаре В.И. Даля встречается старинное название барометра. Какое?',
        'вратарь': 'Так в старину называли сторожа городских ворот.'}
    answer = random.choice([k for k in question.keys()])
    guess = '-' * len(answer)
    print('Можно допустить три ошибки.')
    print('Вопрос:', question[answer])
    # print(answer)
    # print(guess)
    game(answer, guess)


def check_mistakes(mistakes):
    """Функция проверяет количество неверно введенных букв"""
    if mistakes > 3:
        print('Попытки кончились!')
        exit()


def game(answer, guess):
    """Функция проверки введенной буквы или слова целиком."""
    mistakes = 0
    while guess != answer:
        check_mistakes(mistakes)
        user_letter = input('Буква или слово целиком: ').lower()
        if len(user_letter) == 1:
            if user_letter in answer:
                if user_letter not in guess:
                    for index, item in enumerate(answer):
                        if user_letter == item:
                            guess = guess[:index] + user_letter + guess[index + 1:]
                    print('Есть такая буква')
                    print(guess)
                else:
                    print('Такая буква уже есть')
            elif user_letter not in answer:
                print('Нет такой буквы')
                mistakes += 1
        elif len(user_letter) == 0:
            continue
        else:
            if user_letter == answer:
                # print(f'Отлично! Это {answer}!')
                break
            else:
                print('Неверно!')
                mistakes += 1
    print(f'Отлично! Это {answer}!')


if __name__ == '__main__':
    intro()
