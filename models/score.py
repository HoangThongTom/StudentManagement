from utils.database import db


class Score(db.Model):

    __tablename__ = "KETQUAHOCTAP"

    MaSV = db.Column(
        db.String(50),
        db.ForeignKey("SINHVIEN.MaSV"),
        primary_key=True
    )

    MaLHP = db.Column(
        db.String(50),
        db.ForeignKey("LOPHOCPHAN.MaLHP"),
        primary_key=True
    )

    DiemSo = db.Column(db.Float)

    XepLoai = db.Column(db.String(50))