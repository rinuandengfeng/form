from app import db


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.String(2))
    age = db.Column(db.Integer)
    work_place = db.Column(db.String(120))  # 工作单位
    title = db.Column(db.String(60))  # 职称
    position = db.Column(db.String(30))  # 职务
    school = db.Column(db.String(30))  # 毕业院校
    major = db.Column(db.String(30))  # 专业
    education = db.Column(db.String(10))  # 学历
    degree = db.Column(db.String(10))  # 学位
    email = db.Column(db.String(60))  # 邮箱
    wx = db.Column(db.String(40))  # 微信
    tel = db.Column(db.String(11))  # 电话
    work_experience = db.Column(db.Text)  # 主要工作经历
    job = db.Column(db.Text)  # 社会兼职
    photo = db.Column(db.String(120))  # 照片路径

    # 返回全部字段。
    def to_json(self):
        return {
            # "id": self.id,
            "name": self.name,
            "sex": self.sex,
            "age": self.age,
            "work_place": self.work_place,
            "title": self.title,
            # "position": self.position,
            "school": self.school,
            "major": self.major,
            "education": self.education,
            "degree": self.degree,
            "email": self.email,
            # "wx": self.wx,
            "tel": self.tel,
            "work_experience": self.work_experience,
            "job": self.job,
            # "photo": self.photo
        }
