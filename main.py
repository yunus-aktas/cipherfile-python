import tkinter as tk
from tkinter import filedialog, messagebox
import os

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Dosyayı seç",
        filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")]
    )
    if file_path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_path)
        lbl_status.config(text="")

def normalize_key(key: int) -> int:
    return ((key % 26) + 26) % 26

def caesar_shift(text: str, key: int) -> str:
    # key pozitifse şifreler, negatifse çözer (ters kaydırma)
    k = normalize_key(key)
    out = []

    for ch in text:
        if ch.isalpha():
            start = ord('a') if ch.islower() else ord('A')
            out.append(chr((ord(ch) - start + k) % 26 + start))
        else:
            out.append(ch)

    return "".join(out)

def get_key():
    try:
        return int(entry_key.get().strip())
    except ValueError:
        messagebox.showerror("Hata", "Kaydırma anahtarı sayı olmalıdır (örnek: 3).")
        return None

def get_input_path():
    file_path = entry_file.get().strip()
    if not file_path:
        messagebox.showwarning("Uyarı", "Lütfen önce bir dosya seçin.")
        return None
    if not os.path.exists(file_path):
        messagebox.showerror("Hata", f"Dosya bulunamadı:\n{file_path}")
        return None
    return file_path

def encrypt_file():
    file_path = get_input_path()
    if not file_path:
        return

    key = get_key()
    if key is None:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        encrypted = caesar_shift(text, key)

        out_dir = os.path.dirname(file_path)
        out_path = os.path.join(out_dir, "sifreli.txt")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(encrypted)

        lbl_status.config(text=f"✅ Şifrelendi: {out_path}")
        messagebox.showinfo("Başarılı", f"Dosya şifrelendi!\n\nÇıktı:\n{out_path}")

    except UnicodeDecodeError:
        messagebox.showerror(
            "Hata",
            "Dosya UTF-8 olarak okunamadı.\nDosyayı UTF-8 kaydedip tekrar deneyin."
        )
    except Exception as e:
        messagebox.showerror("Hata", f"Beklenmeyen hata:\n{e}")

def decrypt_file():
    file_path = get_input_path()
    if not file_path:
        return

    key = get_key()
    if key is None:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Çözme: aynı algoritma ama ters kaydırma
        decrypted = caesar_shift(text, -key)

        out_dir = os.path.dirname(file_path)
        out_path = os.path.join(out_dir, "cozulmus.txt")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(decrypted)

        lbl_status.config(text=f"✅ Çözüldü: {out_path}")
        messagebox.showinfo("Başarılı", f"Dosya çözüldü!\n\nÇıktı:\n{out_path}")

    except UnicodeDecodeError:
        messagebox.showerror(
            "Hata",
            "Dosya UTF-8 olarak okunamadı.\nDosyayı UTF-8 kaydedip tekrar deneyin."
        )
    except Exception as e:
        messagebox.showerror("Hata", f"Beklenmeyen hata:\n{e}")


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Caesar Dosya Şifreleme / Çözme")
root.geometry("600x260")
root.resizable(False, False)

frame = tk.Frame(root, padx=14, pady=14)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Dosya:").grid(row=0, column=0, sticky="w")

entry_file = tk.Entry(frame, width=60)
entry_file.grid(row=1, column=0, columnspan=2, sticky="we", pady=(4, 8))

btn_browse = tk.Button(frame, text="Dosya Seç", command=browse_file, width=12)
btn_browse.grid(row=1, column=2, padx=(10, 0))

tk.Label(frame, text="Kaydırma anahtarı (örnek: 3):").grid(row=2, column=0, sticky="w", pady=(6, 0))

entry_key = tk.Entry(frame, width=10)
entry_key.insert(0, "3")
entry_key.grid(row=3, column=0, sticky="w", pady=(4, 10))

btn_encrypt = tk.Button(frame, text="Şifrele", command=encrypt_file, width=14)
btn_encrypt.grid(row=3, column=1, sticky="e", pady=(4, 10), padx=(0, 8))

btn_decrypt = tk.Button(frame, text="Çöz", command=decrypt_file, width=14)
btn_decrypt.grid(row=3, column=2, sticky="e", pady=(4, 10))

lbl_status = tk.Label(frame, text="", anchor="w")
lbl_status.grid(row=4, column=0, columnspan=3, sticky="we", pady=(10, 0))

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()
