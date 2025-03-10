sayi = int(input("Bir sayı girin: "))

if sayi < 0:
    print("Negatif sayı girdiniz!")
elif sayi % 2 == 0:
    print("Çift sayı girdiniz!")
else:
    print("Tek sayı girdiniz!")