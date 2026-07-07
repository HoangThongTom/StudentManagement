from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import or_

from utils.database import db
from models.assignment import Assignment

assignment_bp = Blueprint("assignment", __name__)


# ==========================================
# DANH SÁCH PHỤ TRÁCH
# ==========================================
@assignment_bp.route("/assignments")
def assignments():

    keyword = request.args.get("keyword", "")

    if keyword:

        assignment_list = Assignment.query.filter(
            or_(
                Assignment.MaGV.contains(keyword),
                Assignment.MaKhoaHoc.contains(keyword)
            )
        ).all()

    else:

        assignment_list = Assignment.query.all()

    return render_template(
        "assignment/index.html",
        assignments=assignment_list,
        keyword=keyword
    )


# ==========================================
# THÊM
# ==========================================
@assignment_bp.route("/assignments/add", methods=["GET", "POST"])
def add_assignment():

    if request.method == "POST":

        try:

            assignment = Assignment(

                MaGV=request.form["MaGV"],
                MaKhoaHoc=request.form["MaKhoaHoc"]

            )

            db.session.add(assignment)
            db.session.commit()

            flash("Assignment added successfully!", "success")

        except Exception as e:

            db.session.rollback()
            flash(f"Error: {e}", "danger")

        return redirect(url_for("assignment.assignments"))

    return render_template("assignment/add.html")


# ==========================================
# DELETE
# ==========================================
@assignment_bp.route("/assignments/delete/<string:magv>/<string:makh>")
def delete_assignment(magv, makh):

    assignment = Assignment.query.get_or_404((magv, makh))

    try:

        db.session.delete(assignment)
        db.session.commit()

        flash("Assignment deleted!", "danger")

    except Exception as e:

        db.session.rollback()
        flash(f"Error: {e}", "danger")

    return redirect(url_for("assignment.assignments"))