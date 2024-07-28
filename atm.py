users = {
    "1234": {"password": "1234", "balance": 5000, "debt": 1000},
    "5678": {"password": "5678", "balance": 3000, "debt": 500},
    "9101": {"password": "9101", "balance": 10000, "debt": 0}
}

def authenticate_user(card_number):
    password = input("Şifrenizi girin: ")
    if card_number in users and users[card_number]["password"] == password:
        print("Giriş başarılı!")
        return True
    else:
        print("Kart numarası veya şifre yanlış!")
        return False

def bakiye_goruntule(card_number):
    print(f"Güncel bakiyeniz: {users[card_number]['balance']} TL")

def para_yatirma(card_number):
    miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
    users[card_number]['balance'] += miktar
    print(f"{miktar} TL yatırıldı. Güncel bakiyeniz: {users[card_number]['balance']} TL")

def para_cekme(card_number):
    miktar = float(input("Çekmek istediğiniz miktarı girin: "))
    if users[card_number]['balance'] >= miktar:
        users[card_number]['balance'] -= miktar
        print(f"{miktar} TL çekildi. Güncel bakiyeniz: {users[card_number]['balance']} TL")
    else:
        print("Yetersiz bakiye!")

def borc_ode(card_number):
    miktar = float(input("Ödemek istediğiniz borç miktarını girin: "))
    if users[card_number]['balance'] >= miktar:
        if users[card_number]['debt'] >= miktar:
            users[card_number]['balance'] -= miktar
            users[card_number]['debt'] -= miktar
            print(f"{miktar} TL borç ödendi. Güncel bakiyeniz: {users[card_number]['balance']} TL, Güncel borcunuz: {users[card_number]['debt']} TL")
        else:
            print("Girilen miktar borçtan fazla olamaz!")
    else:
        print("Yetersiz bakiye!")

def para_yollama(card_number):
    hedef_kart = input("Para yollamak istediğiniz kart numarasını girin: ")
    miktar = float(input("Göndermek istediğiniz miktarı girin: "))
    if hedef_kart in users:
        if users[card_number]['balance'] >= miktar:
            users[card_number]['balance'] -= miktar
            users[hedef_kart]['balance'] += miktar
            print(f"{miktar} TL {hedef_kart} numaralı hesaba yollandı. Güncel bakiyeniz: {users[card_number]['balance']} TL")
        else:
            print("Yetersiz bakiye!")
    else:
        print("Geçersiz kart numarası!")

def atm_menu(card_number):
    while True:
        print("\n1. Bakiye Görüntüleme\n2. Para Yatırma\n3. Para Çekme\n4. Borç Ödeme\n5. Başka Hesaba Para Yollama\n6. Çıkış")
        secim = input("Yapmak istediğiniz işlemi seçin: ")
        if secim == '1':
            bakiye_goruntule(card_number)
        elif secim == '2':
            para_yatirma(card_number)
        elif secim == '3':
            para_cekme(card_number)
        elif secim == '4':
            borc_ode(card_number)
        elif secim == '5':
            para_yollama(card_number)
        elif secim == '6':
            print("ATM'den çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

def ana_menu():
    while True:
        card_number = input("Kart numaranızı girin (Çıkış için 'q' tuşuna basın): ")
        if card_number.lower() == 'q':
            print("ATM'den çıkılıyor...")
            break
        if authenticate_user(card_number):
            atm_menu(card_number)

ana_menu()
