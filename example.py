# print('Hello World!')
# print('Assalamu alaikum')
# print('''Ashirov
#     Rovshen''')
# print(19//5)
# print(2**4)
# print('Toqqizning kvadrati ', 81, 'ga teng')
# name = 'Ashirov Rovshen'
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize())
# box = '     Sobirjon    '
# print(box.strip())
# onename = input('ismingiz nima ')

# kocha = 'Bog\'bon'
# mahalla = 'Sog\'bon'
# tuman = 'Bodomzor'
# viloyat = 'Samarqand'

# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# kocha = input("Ko'changizni kiriting: ")
# mahalla = input("Mahallangizni kiriting: ")
# tuman = input("Tumaningizni kiriting: ")
# viloyat = input("Viloyatingizni kiriting: ")

# new_address = f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati"

# print(new_address.title())
# print(new_address.upper())
# print(new_address.lower())
# print(new_address.capitalize())
# print(new_address)

# son = int(input('Istalgan son kiriting: \n>>>'))

# son_kv = son**2
# son_kub = son**3

# print(f"{son}ning kvadrati {son_kv}ga teng")
# print(f"{son}ning kubi {son_kub}ga teng")


# age = int(input("Yoshingiz: \n>>>"))

# year = 2021 - age

# print(f"Siz {year}da tug'ilgansiz")

# number1 = int(input("Birinchi sonni kiriting: "))
# number2 = int(input("Ikkinchi sonni kiriting: "))

# print(number1 + number2)
# print(number1 - number2)
# print(number1 * number2)
# print(number1 ** number2)
# print(number1 % number2)
# print(number1 // number2)
# print(number1 / number2)

# names = ["Sobirjon", 'Sardorbek', "Diyorbek", "Tolibjon", "Murodjon"]

# print(f"{names[0]} va {names[1]} bugun yotoqxonada. {names[2]}, {names[3]} va {names[4]} esa uylariga ketishgan.")

# numbers = [23, -3, 7, 3.3]

# numbers[1] = numbers[1] - 44
# numbers[2] = 77

# print(numbers)

# t_shaxslar = ["Muhammad s.a.v.", "Nikolay Tesla", "Ibn Sino"]
# z_shaxslar = ["Elon Musk", "Bobur Akilhanov", " "]

# print(f"Men tarixiy shaxlardan {t_shaxslar.pop(0)} bilan, zamonaviy shaxslardan esa {z_shaxslar.pop(2)} bilan suhbat qilishni istar edim")

# friends = []

# friends.append("Sobirjon")
# friends.append("Sardorbek")
# friends.append("Diyorbek")

# friends.remove("Sardorbek")

# friends.insert(0, "Sardorbek")
# friends.insert(2, "Murodjon")
# friends.insert(4, "Tolibjon")

# print(friends)

# mehmonlar = []

# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(2))

# print(mehmonlar)

# countries = ["uzbekistan", "russia", "turkey", 'japan', "england"]

# print(countries)
# print(len(countries))
# print(sorted(countries))
# print(sorted(countries, reverse=True))

# countries.reverse()

# print(countries)

# countries.sort()

# print(countries)

# countries.sort(reverse=True)

# print(countries)

# numbers = list(range(120, 1201, 2))
# summa = 0

# summa = sum(numbers)

# print(summa)

# value = max(numbers) - min(numbers)

# print(value)
# print(len(numbers))
# print(numbers[:20])
# print(numbers[-20:])
# print(numbers[(len(numbers) // 2 - 10):(len(numbers) // 2 + 10)])

# meals = ["osh", "somsa", "sumalak", "palov", "gamburger"]
# breakfast = meals[:]

# del breakfast[0]
# breakfast.remove("palov")

# breakfast.append("murabbo")
# breakfast.insert(0, "sut")

# print(meals)
# print(breakfast)

# breakfast = tuple(breakfast)

# # breakfast.append("qaymoq va non")

# names = ["Doniyor", "Fayzulla", "Muxriddin", "Ihtirom", "Ahror"]
# sikl = 0

# for name in names:
#     print(f"Salom {name}")
#     sikl = sikl + 1

# print(f"Kod {sikl} marta takrorlandi")

# films = []

# print("5ta eng sevimli kinolaringizni kiriting: ")

# for i in range(5):
#     films.append(input(f"{i+1}-kinoni kiriting: "))

# print(films)

# n = int(input("Bugun nechta kishi bilan suhbat qildingiz: \n>>>"))
# conversation = []

# for i in range(n):
#     conversation.append(input(f"{i+1}-suhbatdoshingizni kiriting: "))

# print(conversation)

# cars = ["toyota", "mazda", "hyundai", "gm", "kia" ]

# for car in cars:
#     if car != "gm":
#         print(car.title()) 
#     else:
#         print(car.upper())

# login = input("Login: \n>>>")

# if login.lower() == "admin":
#     print(f"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login}!")

# num1 = input("Birinchi sonni kiriting: ")
# num2 = input("Ikkinchi sonni kiriting: ")

# if num1 == num2:
#     print("Sonlar teng")

# number = float(input("Istalgan sonni kiriting: "))

# if number < 0:
#     print("Manfiy son")
# else:
#     print("Musbat son")

# number = float(input("Istalgan musbat sonni kiriting: "))

# if number > 0:
#     print(number**0.5)
# else:
#     print("Musbat son kiriting")

# number = int(input("Juft son kiriting: "))

# if number % 2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu juft son emas")

# age = int(input("Yoshingizni kiriting: "))

# if age < 4 or age > 60:
#     narx = 0
# elif age < 18:
#     narx = 10000
# else:
#     narx = 20000

# print(f"Sizga muzeyga kirish {narx} so'm")

# num1 = float(input("Birinchi sonni kiriting: "))
# num2 = float(input("Ikkinchi sonni kiriting: "))

# if num1 == num2:
#     print(f"{num1} = {num2}")
# elif num1 > num2:
#     print(f"{num1} > {num2}")
# else:
#     print(f"{num1} < {num2}")

# mahsulotlar = ["anor", "uzum", "olma", "apelsin", "qovun", "shaftoli", "tarvuz"]
# savat = []

# for i in range(5):
#     savat.append(input(f"Savatga {i+1}-mahsulotni qo'shing: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")

# bor_mahsulotlar = []
# yoq_mahsulotlar = []

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         yoq_mahsulotlar.append(mahsulot)

# if yoq_mahsulotlar:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
    
#     for i in yoq_mahsulotlar:
#         print(i)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# users = ["rovshen", "sardor", "sobirjon", "admin", "adminka"]
# user = input("Login tanlang: ")

# if user.lower() in users:
#     print("login band, yangi login tanlang: ")
# else:
#     print(f"Xush kelibsiz {user}!")

# number = int(input("Istalgan butun son kiriting: "))

# for i in range(2, 11):
#     if number % i == 0:
#         print(f"{number} soni {i} ga qoldiqsiz bo'linadi")


              


