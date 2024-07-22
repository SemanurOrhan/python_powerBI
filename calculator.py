
while True:

    islem =input("Yapmak istediginiz isleme ait numarayi giriniz: \n1-Toplama\n2-Cikarma\n3-Carpma\n4-Bolme\n")
    sonuc=0
    if islem=="1":
        
        sayi1 = float(input("Birinci sayiyi giriniz: "))
        sayi2 = float(input("Ikinci sayiyi giriniz: "))
        sonuc= sayi1+sayi2
        print(f"Sonuc: {sonuc}")
        if int(sonuc)==1837837:
            print("LEBLEBİ")
        

    elif islem=="2":
     
        sayi1 = float(input("Birinci sayiyi giriniz: "))
        sayi2 = float(input("Ikinci sayiyi giriniz: "))
        sonuc=sayi1-sayi2
        print(f"Sonuc: {sonuc}")
        if int(sonuc)==1837837:
            print("LEBLEBİ")

    elif islem=="3":
        
        sayi1 = float(input("Birinci sayiyi giriniz: "))
        sayi2 = float(input("Ikinci sayiyi giriniz: "))
        sonuc= sayi1*sayi2
        print(f"Sonuc: {sonuc}")
        if int(sonuc)==1837837:
            print("LEBLEBİ")

    elif islem=="4":
        
        sayi1 = float(input("Birinci sayiyi giriniz: "))
        sayi2 = float(input("Ikinci sayiyi giriniz: "))

        if sayi2==0:
            print("Bir sayi 0'a bolunemez.")
            continue
        else:
            sonuc= sayi1/sayi2
            print(f"Sonuc: {sonuc}")
            if int(sonuc)==1837837:
                print("LEBLEBİ")

    else:
        print("Hatali giris yaptiniz. Lutfen tekrar deneyiniz.")
        
    devam = input("Başka işlem yapmak istiyor musunuz? (E/H)")
    if devam=="E":
        continue
    elif devam=="H":
        break
        