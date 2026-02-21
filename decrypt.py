def decrypt_file():
    dosya_adi = input("Çözülecek dosya adını girin: ")

    # 🚀 İŞTE PROFESYONEL HATA YAKALAMA KISMI
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            metin = dosya.read()
    except FileNotFoundError:
        print(f"\n⚠️ HATA: Klasörde '{dosya_adi}' adında bir dosya bulunamadı!")
        print("💡 İpucu: Dosya adını yanlış yazmış olabilirsiniz veya henüz şifreleme yapmamış olabilirsiniz.\n")
        return  # Program çökmesin diye işlemi iptal edip menüye döndürüyoruz

    # Eğer dosya varsa, hata vermediyse buradan devam edecek:
    anahtar = int(input("Kaydırma anahtarını girin: "))
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

    print("\n✅ Dosya başarıyla çözüldü!")
    print("📁 Çıktı dosyası: cozulmus.txt\n")
