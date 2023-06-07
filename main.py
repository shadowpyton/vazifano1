# 1
# buyurtmalar = []
#
# while True:
#     mahsulot_nomi = input("mahsulot nomini kiriting (yoki dasturni to'xtatish uchun 'bajarildi' deb yozing): ")
#     if mahsulot_nomi == "bajarildi":
#         break
#     buyurtmalar.append(mahsulot_nomi)
#
# print("Sizning buyurtmalaringiz:", buyurtmalar)
# 2
# mahsulotlar = {}
#
# while True:
#     mahsulot_nomi = input("mahsulot nomini kiriting (yoki dasturni to'xtatish uchun 'bajarildi' deb yozing): ")
#     if mahsulot_nomi == "bajarildi":
#         break
#     mahsulot_narxi = float(input("Enter product price: "))
#     mahsulotlar[mahsulot_nomi] = mahsulot_narxi
#
# print("Mahsulot:", mahsulotlar)
# 3
# e-market lug'ati
magazin = {
    "olma": 5000,
    "banan": 15000,
    "apelsin": 25000,
    "uzum": 20000,
    "tarvuz": 10000
}

# foydalanuvchi buyurtma yo'yxati
buyurtmalar = []

while True:
    mahsulot_nomi = input("mahsulot nomini kiriting (yoki dasturni to'xtatish uchun 'bajarildi' deb yozing): ")
    if mahsulot_nomi == "bajarildi":
        break
    buyurtmalar.append(mahsulot_nomi)

# compare user orders with the e-market
for buyurtma in buyurtmalar:
    if buyurtma in magazin:
        print(f"{buyurtma}: {magazin[buyurtma]}")
    else:
        print(f"Uzur bizda {buyurtma} yo'q")