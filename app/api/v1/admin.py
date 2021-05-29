import os
import time

from flask import Blueprint, request, current_app
from app.models.data import Data

from app import db

admin_bp = Blueprint("admin_bp", __name__)


@admin_bp.route("/home", methods=["POST", "GET"])
def index():
    name = request.form.get('name')
    sex = request.form.get('sex')
    age = request.form.get('age')
    work_place = request.form.get('work_place')
    title = request.form.get('title')
    position = request.form.get('position')
    school = request.form.get('school')
    major = request.form.get('major')
    education = request.form.get('education')
    email = request.form.get('email')
    degree = request.form.get('degree')
    wx = request.form.get('wx')
    tel = request.form.get('tel')
    work_experience = request.form.get('work_experience')
    job = request.form.get('job')
    file = request.files['file']
    t = time.time()
    filename = str(int(t)) + file.filename
    filenamePath = str(current_app.config['BASEAIR'] + os.path.join(current_app.config['UPLOAD_FOLDER'] + filename))
    if file:
        file.save(current_app.config['BASEAIR'] + os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    addInfo = Data(
        name=name,
        sex=sex,
        age=age,
        work_place=work_place,
        title=title,
        position=position,
        school=school,
        major=major,
        education=education,
        degree=degree,
        email=email,
        wx=wx,
        tel=tel,
        work_experience=work_experience,
        job=job,
        photo=filenamePath
    )
    db.session.add(addInfo)   #把数据添加到session中
    db.session.commit()       #提交到数据库中
    return {
        "code": 20000
    }
