from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import or_

from utils.database import db
from models.classroom import Classroom

classroom_bp = Blueprint("classroom", __name__)


# ==========================================
# DANH SÁCH LỚP HỌC PHẦN
# ==========================================
@classroom_bp.route("/classes")
def classes():

    keyword = request.args.get("keyword", "")

    if keyword:

        class_list = Classroom.query.filter(
            or_(
                Classroom.MaLHP.contains(keyword),
                Classroom.MaGV.contains(keyword),
                Classroom.MaKhoaHoc.contains(keyword)
            )
        ).all()

    else:

        class_list = Classroom.query.all()

    return render_template(
        "classroom/index.html",
        classes=class_list,
        keyword=keyword
    )


# ==========================================
# THÊM LỚP HỌC PHẦN
# ==========================================
@classroom_bp.route("/classes/add", methods=["GET", "POST"])
def add_class():

    if request.method == "POST":

        try:

            classroom = Classroom(

                MaLHP=request.form["MaLHP"],
                ThoiGianHoc=request.form["ThoiGianHoc"],
                DiaDiemHoc=request.form["DiaDiemHoc"],
                MaGV=request.form["MaGV"],
                MaKhoaHoc=request.form["MaKhoaHoc"]

            )

            db.session.add(classroom)
            db.session.commit()

            flash("Class added successfully!", "success")

        except Exception as e:

            db.session.rollback()
            flash(f"Error: {e}", "danger")

        return redirect(url_for("classroom.classes"))

    return render_template("classroom/add.html")


# ==========================================
# SỬA LỚP HỌC PHẦN
# ==========================================
@classroom_bp.route("/classes/edit/<string:id>", methods=["GET", "POST"])
def edit_class(id):

    classroom = Classroom.query.get_or_404(id)

    if request.method == "POST":

        try:

            classroom.ThoiGianHoc = request.form["ThoiGianHoc"]
            classroom.DiaDiemHoc = request.form["DiaDiemHoc"]
            classroom.MaGV = request.form["MaGV"]
            classroom.MaKhoaHoc = request.form["MaKhoaHoc"]

            db.session.commit()

            flash("Class updated successfully!", "warning")

        except Exception as e:

            db.session.rollback()
            flash(f"Error: {e}", "danger")

        return redirect(url_for("classroom.classes"))

    return render_template(
        "classroom/edit.html",
        classroom=classroom
    )


# ==========================================
# XÓA LỚP HỌC PHẦN
# ==========================================
@classroom_bp.route("/classes/delete/<string:id>")
def delete_class(id):

    classroom = Classroom.query.get_or_404(id)

    try:

        db.session.delete(classroom)
        db.session.commit()

        flash("Class deleted successfully!", "danger")

    except Exception as e:

        db.session.rollback()
        flash(f"Error: {e}", "danger")

    return redirect(url_for("classroom.classes"))