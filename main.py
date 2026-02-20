# from encrypt import encrypt_file
# from decrypt import decrypt_file

print("1 - Dosya Şifrele")
print("2 - Dosya Çöz")
print("3 - Çıkış")

secim = input("Seçiminizi girin: ")

if secim == "1":
    print("Şifreleme seçildi")
elif secim == "2":
    print("Çözme seçildi")
elif secim == "3":
    print("Çıkış yapılıyor")
else:
    print("Geçersiz seçim")
