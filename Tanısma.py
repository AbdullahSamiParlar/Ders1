import random
import time
print("Merhaba ben Abdullah Sami.")
cevap=input("Sır duymak istermisin?(evet/hayır/ben sır veriyim)")
if cevap == "evet":
    Sirlar = [" Oyun oynamak en sevdiğim iştir","Tavuk sote favori yemeğimdir","Burcum kova","Şubatın 2'sinde doğdum"]
    print(random.choice(Sirlar))
elif cevap== "ben sır veriyim":
    Verilensir=input("Tamam bekliyorum söyle!")
    time.sleep(1)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    a=random.randint(0,5)
    if a==1:
        print(str(Verilensir)+"çok garip!")
    elif a ==2:
        print(str(Verilensir)+"yi ben de severim!")
    else:
        print("Harika!")
    
else:
    print("Tamam")
