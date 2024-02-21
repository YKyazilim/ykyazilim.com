import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunluk = int(input("şifrenizin uzunluğu kaç harflidir?"))
sifre = ""
for i in range(sifre_uzunluk):
    sifre += random.choice(karakterler)
print(sifre)
    
