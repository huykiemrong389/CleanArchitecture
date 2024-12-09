import sqlite3

# Kết nối tới file SQLite
conn = sqlite3.connect("app.db")

# Tạo con trỏ để thực hiện truy vấn
cursor = conn.cursor()

# Liệt kê các bảng
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Lấy dữ liệu từ bảng "users"
cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()
print("Data in 'users':", rows)

# Đóng kết nối
conn.close()
