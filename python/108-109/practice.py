import random

# n = int(input("сколько символов: "))
# n2 = input("какой символ: ")
# print("n2" * n)
#
# stat = int(input("стар:"))
# finish = int(input("конец:"))
# summ_of_numbers = 0
# count_of_numbers = 0
# for i in range(stat, finish + 1):
#     print(i)
#     summ_of_numbers += i
#     print(f"сумма чисел: {summ_of_numbers}")
#     summ_of_numbers += i
#     count_of_numbers += i
# print(f"сумма чисел: {summ_of_numbers}")
# print(f"среднее арифметическое: {summ_of_numbers}")
#
#
# n = int(input("сколько звездочек: "))
# print("spam" * 5)
#
# n = int(input("сколько символов: "))
# n2 = input("какой символ: ")
# print("n2" * n)

score = 0

print("игра на знание таблицы умножения")
print("будет 5 вопросов.")
dif = input("введите уровень сложности от 1 до 4: ")
match dif:
    case "1": start, finish = 1, 5
    case "2": start, finish = 5, 9
    case "3": start, finish = 10, 20
    case "4": start, finish = 20, 99
for i in range(5):
    a = random.randint(start, finish)
    b = random.randint(start, finish)
    print(f" {a} * {b} = ?")
    dif = int(input("Ответ: "))
    if dif == a * b:
        print("верно!")
        score += 1
        print(f"у тебя {score} очков.")
    else:
        print(f"неверно. {a * b}")
