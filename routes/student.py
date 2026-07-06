from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

from utils.database import db
from models.student import Student
from sqlalchemy import or_

student_bp = Blueprint("student", __name__)


# ==========================
# DANH SÁCH SINH VIÊN
# ==========================
@student_bp.route("/students")
def students():

    keyword = request.args.get("keyword", "")

    if keyword:
        student_list = Student.query.filter(
            or_(
                Student.MaSV.contains(keyword),
                Student.HoTen.contains(keyword),
                Student.Email.contains(keyword),
                Student.NganhHoc.contains(keyword)
            )
        ).all()
    else:
        student_list = Student.query.all()

    return render_template(
        "student/index.html",
        students=student_list,
        keyword=keyword
    )

# ==========================
# THÊM SINH VIÊN
# ==========================
@student_bp.route("/students/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        student = Student(
            MaSV=request.form["MaSV"],
            HoTen=request.form["HoTen"],
            GioiTinh=request.form["GioiTinh"],
            NgaySinh=datetime.strptime(
                request.form["NgaySinh"],
                "%Y-%m-%d"
            ).date(),
            NganhHoc=request.form["NganhHoc"],
            Email=request.form["Email"],
            SoDienThoai=request.form["SoDienThoai"],
            DiaChi=request.form["DiaChi"],
            NamNhapHoc=int(request.form["NamNhapHoc"]),
            TrangThaiHocTap=request.form["TrangThaiHocTap"]
        )

        db.session.add(student)
        db.session.commit()

        return redirect(url_for("student.students"))

    return render_template("student/add.html")
# ==========================
# SỬA SINH VIÊN
# ==========================
@student_bp.route("/students/edit/<string:id>", methods=["GET", "POST"])
def edit_student(id):

    student = Student.query.get_or_404(id)

    if request.method == "POST":

        student.HoTen = request.form["HoTen"]
        student.GioiTinh = request.form["GioiTinh"]
        student.NgaySinh = datetime.strptime(
            request.form["NgaySinh"],
            "%Y-%m-%d"
        ).date()

        student.NganhHoc = request.form["NganhHoc"]
        student.Email = request.form["Email"]
        student.SoDienThoai = request.form["SoDienThoai"]
        student.DiaChi = request.form["DiaChi"]
        student.NamNhapHoc = int(request.form["NamNhapHoc"])
        student.TrangThaiHocTap = request.form["TrangThaiHocTap"]

        db.session.commit()

        return redirect(url_for("student.students"))

    return render_template(
        "student/edit.html",
        student=student
    )
# ==========================
# XÓA SINH VIÊN
# ==========================
@student_bp.route("/students/delete/<string:id>")
def delete_student(id):

    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    return redirect(url_for("student.students"))