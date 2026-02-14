# ========================================================
# PROYEK GAME: PELARIAN DARI LAB AI (TEXT ADVENTURE)
# Konsep: Variables, Operators, Print, & Comments
# ========================================================

# --- 1. INISIALISASI GAME (Variables) ---
nama_pemain = "Zidan"
nyawa = 100
energi = 50
level_keamanan = 10  # Skala 1 - 100
status_pintu_terkunci = True

# --- 2. PEMBUKAAN (Print) ---
print("========================================")
print(f" SELAMAT DATANG, {nama_pemain}!")
print(" Anda terjebak di Lab AI yang sedang meledak!")
print("========================================\n")

# --- 3. TANTANGAN 1: KOMPUTER RUSAK (Operators) ---
# Pemain harus menebak angka untuk mematikan laser
print("[!] Ada laser di depanmu!")
angka_kunci = 15
tebakan = 10 # Anggap saja ini input dari pemain

# Menggunakan operator perbandingan dan aritmatika
selisih = angka_kunci - tebakan
energi = energi - 5  # Mengurangi energi karena mencoba

print(f"Mencoba meretas... Selisih angka kunci: {selisih}")
print(f"Sisa energi kamu: {energi}")

# --- 4. TANTANGAN 2: PERANGKAP LISTRIK (Modulo Operator) ---
# Listrik menyambar setiap detik GENAP.
detik_saat_ini = 14
apakah_aman = detik_saat_ini % 2 == 0 # Jika sisa bagi 0, berarti genap

print(f"\nDetik saat ini: {detik_saat_ini}")
print(f"Apakah jalan aman sekarang? {apakah_aman}")

# --- 5. PERHITUNGAN SKOR AKHIR (Complex Operators) ---
# Skor dihitung dari sisa nyawa ditambah energi, dikali bonus level
bonus_level = 1.5
skor_akhir = (nyawa + energi) * bonus_level

# --- 6. STATUS AKHIR (Output) ---
print("\n--- STATUS AKHIR PETUALANGAN ---")
print(f"Pemain       : {nama_pemain}")
print(f"Sisa Nyawa   : {nyawa}%")
print(f"Skor Kamu    : {skor_akhir}")
print("========================================")

# Catatan untuk Guru: 
# Gunakan contoh ini untuk menunjukkan bagaimana variabel 
# berubah sepanjang permainan (Dynamic State).