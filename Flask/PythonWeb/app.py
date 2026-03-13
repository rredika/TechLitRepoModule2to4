from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Step 1: Membuat endpoint untuk memeriksa status API
# @app.route("/")
# def home():
#     return jsonify({
#         "status": "API aktif",
#         "message": "Server berjalan normal"
#     })


# Step 2: Membuat endpoint untuk menampilkan halaman HTML
# @app.route("/")
# def home():
#     return render_template("index.html")

# Step 3: Mengirimkan data binding ke view
@app.route("/")
def home():
    students = [
        {"id": 1, "name": "Alice", "age": 20},
        {"id": 2, "name": "Bob", "age": 22},
        {"id": 3, "name": "Charlie", "age": 21}
    ]
    return render_template("index.html", data=students)


if __name__ == "__main__":
    app.run(debug=True)