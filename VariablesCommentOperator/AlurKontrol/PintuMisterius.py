# Project Mini: Pintu Misterius
# Konsep: Alur Kontrol (if, else, elif) dan Perulangan (while)

print("=== SELAMAT DATANG DI THE ADVENTURE GAME ===")
print("Kamu berada di depan tiga pintu misterius.")
print("Ketik '0' untuk menyerah dan keluar dari permainan.")

# Challenge Bonus: Menggunakan while loop agar game tidak langsung berhenti
game_berjalan = True

while game_berjalan:
    print("\n---")
    # Mengambil input dari pengguna
    pilihan = input("Pilih pintu (1, 2, atau 3): ")

    # 1. Cek apakah pengguna ingin keluar
    if pilihan == '0':
        print("Terima kasih sudah bermain! Sampai jumpa lagi.")
        game_berjalan = False  # Mengubah kondisi agar loop berhenti
    
    # 2. Logika pintu menggunakan if-elif-else
    elif pilihan == '1':
        print(">> [PINTU 1]: Kamu menemukan peti berisi EMAS! Kamu kaya raya!")
    
    elif pilihan == '2':
        print(">> [PINTU 2]: Ups, ada NAGA tidur! Kamu harus lari pelan-pelan agar tidak dimakan.")
    
    elif pilihan == '3':
        print(">> [PINTU 3]: Ruangan ini KOSONG. Hanya ada debu dan sarang laba-laba.")
    
    # 3. Menangani input yang salah
    else:
        print(">> [ERROR]: Pilihan tidak valid! Masukkan angka 1, 2, 3, atau 0.")

print("============================================")