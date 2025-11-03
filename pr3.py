password = "password123"
user_input = "password123"
if user_input == password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")
day_number = 3
days = {
    1: "Понеділок",
    2: "Вівторок",
    3: "Середа",
    4: "Четвер",
    5: "П’ятниця",
    6: "Субота",
    7: "Неділя"
}
if 1 <= day_number <= 7:
    print(days[day_number])
else:
    print("Помилка: некоректний номер дня тижня")

num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
numbers = [1, 2, 3, 4, 5]
total = 0
for n in numbers:
    total += n
print("Сума чисел:", total)
fact_num = 5
factorial = 1
for i in range(1, fact_num + 1):
    factorial *= i
print(f"Факторіал {fact_num} = {factorial}")

for i in range(2, 51, 2):
    print(i, end=' ')
print()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(1, 31) if is_prime(x)]
print("Прості числа від 1 до 30:", primes)
lst = [1, 2, 3]
lst.append(4)
lst.append(5)
if 10 in lst:
    lst.remove(10)
print(lst)

lst2 = [1, 2, 3, 4, 5]
print(sum(lst2))
lst3 = [1, 2, 3]
dbl_lst = [x * 2 for x in lst3]
print(dbl_lst)

fruits = ("яблуко", "банан", "апельсин")
for fruit in fruits:
    print(fruit)
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)
athlete = {"ім'я": "Лео", "вік": 30, "спорт": "футбол", "команда": "Барселона"}
for key, value in athlete.items():
    print(f"{key}: {value}")
books = {"1984": 1949, "Гаррі Поттер": 1997}
books["Віднесені вітром"] = 1936
print(books)
capitals = {"Україна": "Київ", "Франція": "Париж", "Німеччина": "Берлін"}
country = "Україна"
if country in capitals:
    print(capitals[country])
else:
    print("Країна не знайдена")
