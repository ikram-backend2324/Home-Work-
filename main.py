# Magliwmatlar turleri

# #1
# name = 'Джон'
# admin = name
# print(admin)

# #2
#
# a1 = 5+3
# a2 = 5-3
# a3 = 5*3
# a4 = 5/3
# a5 = 5**3
#
# print(f"a1 = {a1}, a2 = {a2}, a3 = {a3}, a4 = {float(a4)}, a5 = {a5}")

#3
# #
# a6 = 5 % 3
# a7 = 3 % 5
# a8 = 5+3
# a9 = 5-3
# a10 = str(75) + 'кг'
# print(f"a6 = {a6}, a7 = {a7}, a8 = {a8}, a9 = {a9}, a10 = {a10}")


#4

# # 1-variant
#
# height = 23
# width = 10
# s = height*width
# print(s)
#

# # 2-variant
#
# height = int(input())
# width = int(input())
# s = height*width
# print(s)

# Shartli operatorlar

# # 1
# a = int(input("A = "))
#
# if a == '10':
#     print('Верно')
# else :
#     print('Неверно')

# # 2
#
# min = int(input("Min = "))
#
# if min <= 24:
#     if 0 < min < 12:
#         print("Azan")
#     if 12 < min < 17:
#         print("Tus")
#     if 17 < min < 21:
#         print("Kesh")
#     if 21 < min <= 24:
#         print("Tun")
# elif min > 24:
#     if min>48:
#         min -=48
#         if 0 < min < 12:
#             print("Azan")
#         if 12 < min < 17:
#             print("Tus")
#         if 17 < min < 21:
#             print("Kesh")
#         if 21 < min <= 24:
#             print("Tun")
#
#     else:
#         min -= 24
#         if 0 < min < 12:
#             print("Azan")
#         if 12 < min < 17:
#             print("Tus")
#         if 17 < min < 21:
#             print("Kesh")
#         if 21 < min <= 24:
#             print("Tun")

#
# #3
#
# a = int(input("a = "))
#
# if a>1:
#     print("а больше 1")
# else:
#     print("«а не больше 1»")

# 4
# year = int(input("возраст: "))
#
# if year<20:
#     print("«Вы слишком молоды»")
# else:
#     print("«Вы нам подходите»")
#

# 5

# question = input("Atinizdi kiritiwdi qaleysizbe: (yes/no) ")
#
# if question.lower() == 'yes':
#     name = input("Atinizdi kiritin: ")
#     print(f"Привет, {name}!")
# else:
#     print("Привет, незнакомец!")

# # 6
#
# password = input('PASSWORD: ')
# if password == ('9583' or '1747'):
#     print("доступны модули баз А, В и С")
# if password == ('3331' or '7922'):
#     print("доступны модули баз В и С")
# if password == ("9455" or "8997"):
#     print("доступен модуль базы С")
