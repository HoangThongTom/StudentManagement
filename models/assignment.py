from utils.database import db


class Assignment(db.Model):

    __tablename__ = "PHUTRACH"

    MaGV = db.Column(db.String(50), primary_key=True)
    MaKhoaHoc = db.Column(db.String(50), primary_key=True)