from encrypt import encrypt_file
from decrypt import decrypt_file

while True:
    print("\n--- DOSYA ŞİFRELEME PROGRAMI ---")
    print("1 - Dosya Şifrele")
    print("2 - Dosya Çöz")
    print("3 - Çıkış")

    secim = input("Seçiminizi girin: ")

    if secim == "1":
        encrypt_file()

    elif secim == "2":
        decrypt_file()

    elif secim == "3":
        print("Çıkış yapılıyor... 👋")
        break

    else:
        print("❌ Geçersiz seçim! Lütfen 1, 2 veya 3 girin.")
