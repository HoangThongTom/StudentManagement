from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import or_

from utils.database import db
from models.subject import Subject

subject_bp = Blueprint("subject", __name__)


# ==========================================
# DANH SÁCH MÔN HỌC + TÌM KIẾM
# ==========================================
@subject_bp.route("/subjects")
def subjects():

    keyword = request.args.get("keyword", "")

    if keyword:

        subject_list = Subject.query.filter(
            or_(
                Subject.MaKhoaHoc.contains(keyword),
                Subject.TenKhoaHoc.contains(keyword)
            )
        ).all()

    else:

        subject_list = Subject.query.all()

    return render_template(
        "subject/index.html",
        subjects=subject_list,
        keyword=keyword
    )


# ==========================================
# THÊM MÔN HỌC
# ==========================================
@subject_bp.route("/subjects/add", methods=["GET", "POST"])
def add_subject():

    if request.method == "POST":

        try:

            subject = Subject(

                MaKhoaHoc=request.form["MaKhoaHoc"],
                TenKhoaHoc=request.form["TenKhoaHoc"],
                MoTa=request.form["MoTa"],
                SoTinChi=int(request.form["SoTinChi"])

            )

            db.session.add(subject)
            db.session.commit()

            flash("Subject added successfully!", "success")

        except Exception as e:

            db.session.rollback()
            flash(f"Error: {e}", "danger")

        return redirect(url_for("subject.subjects"))

    return render_template("subject/add.html")


# ==========================================
# SỬA MÔN HỌC
# ==========================================
@subject_bp.route("/subjects/edit/<string:id>", methods=["GET", "POST"])
def edit_subject(id):

    subject = Subject.query.get_or_404(id)

    if request.method == "POST":

        try:

            subject.TenKhoaHoc = request.form["TenKhoaHoc"]
            subject.MoTa = request.form["MoTa"]
            subject.SoTinChi = int(request.form["SoTinChi"])

            db.session.commit()

            flash("Subject updated successfully!", "warning")

        except Exception as e:

            db.session.rollback()
            flash(f"Error: {e}", "danger")

        return redirect(url_for("subject.subjects"))

    return render_template(
        "subject/edit.html",
        subject=subject
    )


# ==========================================
# XÓA MÔN HỌC
# ==========================================
@subject_bp.route("/subjects/delete/<string:id>")
def delete_subject(id):

    subject = Subject.query.get_or_404(id)

    try:

        db.session.delete(subject)
        db.session.commit()

        flash("Subject deleted successfully!", "danger")

    except Exception as e:

        db.session.rollback()
        flash(f"Error: {e}", "danger")

    return redirect(url_for("subject.subjects"))