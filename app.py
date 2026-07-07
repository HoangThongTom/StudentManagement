from flask import Flask, render_template
from sqlalchemy import func

# Đọc cấu hình
from config import Config

# Kết nối Database
from utils.database import db

# Models
from models.student import Student
from models.lecturer import Lecturer
from models.subject import Subject
from models.score import Score

# Blueprints
from routes.student import student_bp
from routes.lecturer import lecturer_bp
from routes.subject import subject_bp
from routes.classroom import classroom_bp
from routes.score import score_bp
from routes.assignment import assignment_bp

# =====================================================
# KHỞI TẠO ỨNG DỤNG FLASK
# =====================================================
app = Flask(__name__)

# Đọc cấu hình
app.config.from_object(Config)

# Khởi tạo SQLAlchemy
db.init_app(app)

# =====================================================
# ĐĂNG KÝ BLUEPRINT
# =====================================================
app.register_blueprint(student_bp)
app.register_blueprint(lecturer_bp)
app.register_blueprint(subject_bp)
app.register_blueprint(classroom_bp)
app.register_blueprint(score_bp)
app.register_blueprint(assignment_bp)

# =====================================================
# DASHBOARD
# =====================================================
@app.route("/")
def index():

    # Tổng số sinh viên
    total_students = Student.query.count()

    # Tổng số giảng viên
    total_lecturers = Lecturer.query.count()

    # Tổng số môn học
    total_subjects = Subject.query.count()

    # GPA trung bình
    average_gpa = (
        db.session.query(func.avg(Score.DiemSo)).scalar() or 0
    )
    average_gpa = round(average_gpa, 2)

    # 5 sinh viên mới nhất
    recent_students = (
        Student.query
        .order_by(Student.MaSV.desc())
        .limit(5)
        .all()
    )

    return render_template(
        "dashboard.html",
        total_students=total_students,
        total_lecturers=total_lecturers,
        total_subjects=total_subjects,
        average_gpa=average_gpa,
        recent_students=recent_students
    )

# =====================================================
# KIỂM TRA KẾT NỐI DATABASE
# =====================================================
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

# =====================================================
# CHẠY SERVER
# =====================================================
if __name__ == "__main__":
    app.run(debug=True)