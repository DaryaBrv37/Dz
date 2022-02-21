name = "Darya"
print(name)

age = 20
print('Мне', age, 'лет')

name5 = name * 5
print(name5)

user_name = input("Введите имя:")
user_age = input('Введите возраст:')
print('Доброго времени суток,', user_name)

my_age = int(input('Возраст:'))
if my_age < 7:
    print('пора собирать игрушки')
elif 7 < my_age < 17:
    print('пора делать уроки')
elif 17 < my_age < 90:
    print('ты уже вырос')
else:
    print('странный возраст')
length = len(user_name)
print(user_name [1:length - 1:])
print(user_name[::-1])
print(user_name[-3::])
print(user_name[:5:])

b = len(user_name)
print('Длина имени пользователя:', b)

num = b
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма =: ", sum)

num = b
mult = 1
while (num != 0):
    mult = mult * (num % 10)
    num = num // 10
print("Произведение =: ", mult)

name_U = str(str.upper(user_name))
name_L = str(str.lower(user_name))
name_UL = name_U[0:1:] + name_L[1::]
name_LU = name_L[0:1:] + name_U[1::]
print(name_U, name_L, name_UL, name_LU)

try:
    test = int(user_name)
    print('Вы ввели все верно!', test)
except:
    print('Ошибка!')
try:
    user_name = input("Введите имя:")
    a.replace(' ')
    print('Верно')
except ValueError:
    print('Ошибочка вышла')
try:
    a = user_age
    if 0 < a < 150:
        print('Верно!')
except Exception:
    print('нужно верное число')

print('Реши задачу 2 * 2 * 128**2 / 2 + 45')
a = 2*2 #4
b = 4 * 128 #512
c = b**2 #262144.
d = c / 2 #131072
g = d + 45
otv = input('Введите ответ:')
try:
    otv = 131117
except Exception:
    print('Посчитай еще раз')

