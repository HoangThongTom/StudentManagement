from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import or_

from utils.database import db
from models.lecturer import Lecturer

lecturer_bp = Blueprint("lecturer", __name__)


# ==========================================
# DANH SÁCH GIẢNG VIÊN
# ==========================================
@lecturer_bp.route("/lecturers")
def lecturers():

    keyword = request.args.get("keyword", "")

    if keyword:

        lecturer_list = Lecturer.query.filter(
            or_(
                Lecturer.MaGV.contains(keyword),
                Lecturer.TenGV.contains(keyword),
                Lecturer.Email.contains(keyword),
                Lecturer.BoMon.contains(keyword)
            )
        ).all()

    else:

        lecturer_list = Lecturer.query.all()

    return render_template(
        "lecturer/index.html",
        lecturers=lecturer_list,
        keyword=keyword
    )


# ==========================================
# THÊM GIẢNG VIÊN
# ==========================================
@lecturer_bp.route("/lecturers/add", methods=["GET", "POST"])
def add_lecturer():

    if request.method == "POST":

        try:

            lecturer = Lecturer(

                MaGV=request.form["MaGV"],
                TenGV=request.form["TenGV"],
                BoMon=request.form["BoMon"],
                Email=request.form["Email"],
                ChuyenNganh=request.form["ChuyenNganh"],
                SoDienThoai=request.form["SoDienThoai"]

            )

            db.session.add(lecturer)
            db.session.commit()

            flash("Lecturer added successfully!", "success")

        except Exception as e:

            db.session.rollback()
            flash(f"Error: {e}", "danger")

        return redirect(url_for("lecturer.lecturers"))

    return render_template("lecturer/add.html")


# ==========================================
# SỬA GIẢNG VIÊN
# ==========================================
@lecturer_bp.route("/lecturers/edit/<string:id>", methods=["GET", "POST"])
def edit_lecturer(id):

    lecturer = Lecturer.query.get_or_404(id)

    if request.method == "POST":

        try:

            lecturer.TenGV = request.form["TenGV"]
            lecturer.BoMon = request.form["BoMon"]
            lecturer.Email = request.form["Email"]
            lecturer.ChuyenNganh = request.form["ChuyenNganh"]
            lecturer.SoDienThoai = request.form["SoDienThoai"]

            db.session.commit()

            flash("Lecturer updated successfully!", "warning")

        except Exception as e:

            db.session.rollback()
            flash(f"Error: {e}", "danger")

        return redirect(url_for("lecturer.lecturers"))

    return render_template(
        "lecturer/edit.html",
        lecturer=lecturer
    )


# ==========================================
# XÓA GIẢNG VIÊN
# ==========================================
@lecturer_bp.route("/lecturers/delete/<string:id>")
def delete_lecturer(id):

    lecturer = Lecturer.query.get_or_404(id)

    try:

        db.session.delete(lecturer)
        db.session.commit()

        flash("Lecturer deleted successfully!", "danger")

    except Exception as e:

        db.session.rollback()
        flash(f"Error: {e}", "danger")

    return redirect(url_for("lecturer.lecturers"))