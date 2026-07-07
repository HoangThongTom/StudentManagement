from utils.database import db


class Classroom(db.Model):

    __tablename__ = "LOPHOCPHAN"

    MaLHP = db.Column(db.String(50), primary_key=True)
    ThoiGianHoc = db.Column(db.String(100))
    DiaDiemHoc = db.Column(db.String(100))
    MaGV = db.Column(db.String(50))
    MaKhoaHoc = db.Column(db.String(50))

    scores = db.relationship(
    "Score",
    backref="classroom",
    lazy=True,
    cascade="all, delete"
)