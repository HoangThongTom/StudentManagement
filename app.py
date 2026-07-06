from flask import Flask, render_template
from config import Config
from utils.database import db
from routes.student import student_bp

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Đọc cấu hình
app.config.from_object(Config)

# Khởi tạo SQLAlchemy
db.init_app(app)

# Đăng ký Blueprint
app.register_blueprint(student_bp)


# ===========================
# ROUTE TRANG CHỦ
# ===========================
@app.route("/")
def index():
    return render_template("dashboard.html")


# ===========================
# KIỂM TRA KẾT NỐI DATABASE
# ===========================
with app.app_context():
    try:
        db.engine.connect()
        print("===================================")
        print(" MySQL Connected Successfully!")
        print("===================================")
    except Exception as e:
        print("===================================")
        print(" Database Connection Failed!")
        print(e)
        print("===================================")


# ===========================
# CHẠY SERVER
# ===========================
if __name__ == "__main__":
    app.run(debug=True)