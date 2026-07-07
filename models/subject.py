from utils.database import db


class Subject(db.Model):

    __tablename__ = "KHOAHOC"

    MaKhoaHoc = db.Column(db.String(50), primary_key=True)
    TenKhoaHoc = db.Column(db.String(255), nullable=False)
    MoTa = db.Column(db.Text)
    SoTinChi = db.Column(db.Integer)