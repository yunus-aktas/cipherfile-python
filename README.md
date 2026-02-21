# 🔐 CipherFile – Python Dosya Şifreleme Projesi

## 📌 Proje Amacı
Bu proje, Python programlama dili kullanılarak
metin dosyalarının şifrelenmesi ve şifrelerinin çözülmesi amacıyla geliştirilmiştir.

Proje kapsamında temel şifreleme algoritmaları,
dosya okuma/yazma işlemleri ve hata yakalama yapıları uygulanmıştır.

---

## 🧠 Kullanılan Şifreleme Algoritması
Bu projede **Caesar Cipher (Kaydırmalı Şifreleme)** yöntemi kullanılmıştır.

Bu algoritmada:
- Metindeki her harf, alfabede belirli bir sayı kadar ileri kaydırılır.
- Şifre çözme işleminde bu kaydırma geri alınır.
- Büyük ve küçük harfler korunur.

---

## ✨ Özellikler
- Metin dosyalarını şifreleme
- Şifrelenmiş dosyaların çözülmesi
- Caesar Cipher algoritması kullanımı
- Büyük / küçük harf duyarlılığı
- Dosya okuma ve yazma işlemleri
- Hata yakalama (dosya bulunamazsa uyarı)
- Menü tabanlı kullanıcı arayüzü

---

## 📁 Proje Dosya Yapısı


cipherfile-python/
│
├── main.py # Ana menü ve program kontrolü
├── encrypt.py # Dosya şifreleme işlemleri
├── decrypt.py # Dosya şifre çözme işlemleri
├── README.md # Proje açıklaması
└── metin.txt # Test dosyası



---

## ▶️ Program Nasıl Çalıştırılır?

1. Proje bilgisayara indirilir.
2. Proje klasöründe terminal / komut penceresi açılır.
3. Aşağıdaki komut çalıştırılır:



python main.py


---

## 🧪 Örnek Kullanım

**Giriş dosyası (metin.txt):**

Merhaba hocam
Bu bir test dosyasidir



**Şifreleme anahtarı:** 3

**Oluşan şifreli dosya (sifreli.txt):**


Phukded krfdp
Ex elu whvw grvbvlglu



**Çözülen dosya (cozulmus.txt):**


Merhaba hocam
Bu bir test dosyasidir



---

## 🔄 Program Akışı
1. Program başlatılır
2. Kullanıcıya menü gösterilir
3. Kullanıcı şifreleme veya çözme işlemi seçer
4. Dosya adı ve anahtar alınır
5. İşlem gerçekleştirilir
6. Sonuç kullanıcıya gösterilir
7. Menü tekrar görüntülenir

---

## ⚠️ Hata Durumları
- Dosya bulunamazsa kullanıcı uyarılır
- Hatalı seçimlerde menü tekrar gösterilir
- Program çökmeden çalışmaya devam eder

---

## 🔮 Gelecekte Geliştirilebilecek Özellikler
- Farklı şifreleme algoritmalarının eklenmesi
- Grafik arayüz (GUI) desteği
- Anahtar doğrulama sistemi
- Farklı dosya türlerinin desteklenmesi

---

## 👨‍💻 Geliştirici
Yunus Aktaş

Bu proje eğitim amaçlı geliştirilmiştir.
