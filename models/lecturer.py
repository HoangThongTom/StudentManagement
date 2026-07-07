from utils.database import db


class Lecturer(db.Model):

    __tablename__ = "GIANGVIEN"

    MaGV = db.Column(db.String(50), primary_key=True)
    TenGV = db.Column(db.String(255), nullable=False)
    BoMon = db.Column(db.String(100))
    Email = db.Column(db.String(100), unique=True)
    ChuyenNganh = db.Column(db.String(150))
    SoDienThoai = db.Column(db.String(15))