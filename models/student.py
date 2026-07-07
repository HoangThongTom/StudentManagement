from utils.database import db


class Student(db.Model):
    __tablename__ = "SINHVIEN"

    MaSV = db.Column(db.String(50), primary_key=True)
    HoTen = db.Column(db.String(255), nullable=False)
    GioiTinh = db.Column(db.String(10))
    NgaySinh = db.Column(db.Date)
    NganhHoc = db.Column(db.String(150))
    Email = db.Column(db.String(100), unique=True)
    SoDienThoai = db.Column(db.String(15))
    DiaChi = db.Column(db.String(255))
    NamNhapHoc = db.Column(db.Integer)
    TrangThaiHocTap = db.Column(db.String(50))

    scores = db.relationship(
    "Score",
    backref="student",
    lazy=True,
    cascade="all, delete"
)