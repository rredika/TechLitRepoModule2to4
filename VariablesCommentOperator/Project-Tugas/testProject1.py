nama_pemain = "Siswa_IT"
nyawa = 100
energi = 50
angka_kunci = 15
tebakan = 10
detik_saat_ini = 14
bonus_level = 1.5

print(f"========================================"
      f"\n SELAMAT DATANG, {nama_pemain}!"
      f"\n Anda terjebak di Lab AI yang sedang meledak!" 
      f"\n========================================\n")

energi = energi - 5
selisih = angka_kunci - tebakan
skor_akhir = ((nyawa + energi) * bonus_level)
apakah_aman = detik_saat_ini % 2 == 0

print(f"Apakah aman sekarang ? {apakah_aman}")