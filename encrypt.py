def encrypt_file():
    # Kullanıcıdan dosya adı al
    input_file = input("Şifrelenecek dosya adını girin (ornek: metin.txt): ")
    
    # Kaydırma anahtarı
    key = int(input("Kaydırma anahtarını girin (ornek: 3): "))

    # Dosyayı oku
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    encrypted_text = ""

    # Caesar Cipher algoritması
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - start + key) % 26 + start)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    # Şifreli dosyayı yaz
    with open("sifreli.txt", "w", encoding="utf-8") as file:
        file.write(encrypted_text)

    print("✅ Dosya başarıyla şifrelendi!")
    print("📄 Çıktı dosyası: sifreli.txt")# Bu dosya sifreleme (encrypt) islemlerini icerecek
# Caesar Cipher algoritmasi burada yazilacak
