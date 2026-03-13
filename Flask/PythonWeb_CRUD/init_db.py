import sqlite3

# koneksi database (file otomatis dibuat kalau belum ada)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# buat tabel users
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    level TEXT NOT NULL
)
""")

# data dummy
data_users = [
    ("Andi Saputra", "andi", "12345", "admin"),
    ("Budi Hartono", "budi", "12345", "user"),
    ("Citra Lestari", "citra", "12345", "user"),
    ("Dewi Anggraini", "dewi", "12345", "kasir"),
    ("Eko Pratama", "eko", "12345", "user"),
]

# insert data
cursor.executemany("""
INSERT OR IGNORE INTO users (nama, username, password, level)
VALUES (?, ?, ?, ?)
""", data_users)

conn.commit()
conn.close()

print("Database + tabel users + data dummy berhasil dibuat.")
