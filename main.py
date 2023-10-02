import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" #şifrenin içinde olmasını istediğin karakterler

sayi = int(input("Şifreniz kaç haneli olsun? "))

sifre = ""
for i in range(sayi):
    x = random.choice(karakterler)
    sifre = sifre + x


print(sifre)
