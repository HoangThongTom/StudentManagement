from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import or_

from utils.database import db
from models.score import Score
from models.student import Student
from models.classroom import Classroom

score_bp = Blueprint("score", __name__)


# ==========================================
# DANH SÁCH ĐIỂM
# ==========================================
@score_bp.route("/scores")
def scores():

    keyword = request.args.get("keyword", "")

    if keyword:

        score_list = Score.query.filter(
            or_(
                Score.MaSV.contains(keyword),
                Score.MaLHP.contains(keyword)
            )
        ).all()

    else:

        score_list = Score.query.all()

    return render_template(
        "score/index.html",
        scores=score_list,
        keyword=keyword
    )


# ==========================================
# THÊM ĐIỂM
# ==========================================
@score_bp.route("/scores/add", methods=["GET", "POST"])
def add_score():

    students = Student.query.all()
    classrooms = Classroom.query.all()

    if request.method == "POST":

        score = Score(

            MaSV=request.form["MaSV"],
            MaLHP=request.form["MaLHP"],
            DiemSo=float(request.form["DiemSo"]),
            XepLoai=request.form["XepLoai"]

        )

        db.session.add(score)
        db.session.commit()

        flash("Score added successfully!", "success")

        return redirect(url_for("score.scores"))

    return render_template(
        "score/add.html",
        students=students,
        classrooms=classrooms
    )


# ==========================================
# SỬA ĐIỂM
# ==========================================
@score_bp.route("/scores/edit/<string:masv>/<string:malhp>", methods=["GET", "POST"])
def edit_score(masv, malhp):

    score = Score.query.get_or_404((masv, malhp))

    if request.method == "POST":

        try:

            score.DiemSo = float(request.form["DiemSo"])
            score.XepLoai = request.form["XepLoai"]

            db.session.commit()

            flash("Score updated successfully!", "warning")

        except Exception as e:

            db.session.rollback()
            flash(f"Error: {e}", "danger")

        return redirect(url_for("score.scores"))

    return render_template(
        "score/edit.html",
        score=score
    )


# ==========================================
# XÓA ĐIỂM
# ==========================================
@score_bp.route("/scores/delete/<string:masv>/<string:malhp>")
def delete_score(masv, malhp):

    score = Score.query.get_or_404((masv, malhp))

    try:

        db.session.delete(score)
        db.session.commit()

        flash("Score deleted successfully!", "danger")

    except Exception as e:

        db.session.rollback()
        flash(f"Error: {e}", "danger")

    return redirect(url_for("score.scores"))