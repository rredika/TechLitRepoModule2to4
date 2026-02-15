harga_sepatu = 120000
harga_topi = 45000

total = harga_sepatu + harga_topi

# Cek gratis ongkir (Minimal belanja 150rb)
gratis_ongkir = total > 150000

print("Total Belanja: Rp", total)
print("Dapat Gratis Ongkir?", gratis_ongkir)


suhu = 100
batas_suhu_aman = 20
suhu_sekarang = 15
suhu_bahaya = False
suhu_bahaya = suhu_sekarang < batas_suhu_aman

print("Suhu Sekarang:", suhu_sekarang)


