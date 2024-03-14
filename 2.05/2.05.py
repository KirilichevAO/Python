# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))

three_number = number % 10
two_number = number // 10 % 10
one_number = number // 100

print(f'{number} -> {one_number + two_number + three_number} ({one_number} + {two_number} + {three_number})')
