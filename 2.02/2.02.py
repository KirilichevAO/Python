# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32

one_class = int(input('Введите численность первого класса: '))
two_class = int(input('Введите численность второго класса: '))
three_class = int(input('Введите численность третьего класса: '))

desks_one_class = (one_class + 1) // 2
desks_two_class = (two_class + 1) // 2
desk_three_class = (three_class + 1) // 2

print(f'Нужно {desks_one_class + desks_two_class + desk_three_class} парт.')
