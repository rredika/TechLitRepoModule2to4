# ==========================================
# PROYEK: SISTEM KONTROL KOLONI MARS v1.0
# Modul: Print, Comment, Variable, Operator
# ==========================================

# 1. IDENTITAS DATA (Module: Variables & Comments)
# Menyimpan informasi dasar astronot
nama_astronot = "Budi Perkasa"
usia_bumi = 16
berat_bumi = 65.0  # dalam kg
oksigen_persen = 100

# 2. KALKULASI FISIKA MARS (Module: Operators)
# Di Mars, berat benda hanya 38% dari berat di Bumi
berat_mars = berat_bumi * 0.38

# Satu tahun di Mars sekitar 687 hari Bumi
usia_mars = (usia_bumi * 365) / 687

# 3. STATUS LOGISTIK (Module: Operators & Comparison)
# Simulasi konsumsi sumber daya
jumlah_makanan_kaleng = 50
hari_misi = 12
makanan_per_hari = 2

sisa_makanan = jumlah_makanan_kaleng - (hari_misi * makanan_per_hari)
apakah_makanan_cukup = sisa_makanan > 10  # Cek jika sisa lebih dari 10 kaleng

# 4. LAPORAN MONITOR (Module: Print)
print("------------------------------------------")
print("   LAPORAN HARIAN KOLONI MARS: SOL 12    ")
print("------------------------------------------")

# Menggunakan f-string (fitur modern Python untuk menggabungkan variabel)
print(f"Astronot Bertugas : {nama_astronot}")
print(f"Usia Anda di Mars : {usia_mars:.2f} tahun")
print(f"Berat Anda di Mars: {berat_mars} kg")

print("\n--- STATUS LOGISTIK ---")
print(f"Sisa Oksigen      : {oksigen_persen}%")
print(f"Sisa Stok Makanan : {sisa_makanan} kaleng")
print(f"Stok Aman?        : {apakah_makanan_cukup}")

# 5. TANTANGAN LOGIKA (Module: Operators)
# Operator Modulo untuk menentukan jadwal piket (Ganjil/Genap)
jadwal_piket = hari_misi % 2 
print(f"\nKode Jadwal Piket : {jadwal_piket} (0=Maintenance, 1=Research)")
print("------------------------------------------")