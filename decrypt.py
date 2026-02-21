def decrypt_file():
    dosya_adi = input("Çözülecek dosya adını girin: ")
    anahtar = int(input("Kaydırma anahtarını girin: "))

    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        metin = dosya.read()

    cozulen_metin = ""

    for karakter in metin:
        if karakter.isalpha():
            baslangic = ord('A') if karakter.isupper() else ord('a')
            cozulen = chr((ord(karakter) - baslangic - anahtar) % 26 + baslangic)
            cozulen_metin += cozulen
        else:
            cozulen_metin += karakter

    with open("cozulmus.txt", "w", encoding="utf-8") as dosya:
        dosya.write(cozulen_metin)

    print("Dosya başarıyla çözüldü!")
    print("Çıktı dosyası: cozulmus.txt")
