import wtforms # 定义字段
from flask_wtf import Form # 定义表单
from wtforms import validators # 定义校验
from FlaskStudent.models import Course

course_list = [(c.id,c.name) for c in Course.query.all()]

class TeacherForm(Form):
    """
    form字段的参数
    label=None, 表单的标签
    validators=None, 校验，传入校验的方法
    filters=tuple(), 过滤
    description='',  描述
    id=None, html id
    default=None, 默认值
    widget=None, 样式
    render_kw=None, 属性 参数
    """

    name = wtforms.StringField(
        label="教师姓名",
        render_kw={
            "class": "form-control",
            "placeholder": "教师姓名"
        },
        validators=[
            validators.DataRequired("姓名不可以为空")
        ]
    )
    age = wtforms.IntegerField(
        label="教师年龄",
        render_kw={
            "class": "form-control",
            "placeholder": "教师年龄"
        },
        validators=[
            validators.DataRequired("年龄不可以为空")
        ]
    )
    gender = wtforms.SelectField(
        label="教师性别",
        render_kw={
            "class": "form-control",
        },
        choices=[
            ("1","男"),
            ("2","女")
        ]
    )
    course = wtforms.SelectField(
        label="学科",
        render_kw={
            "class": "form-control",
        },
        choices=course_list
    )
    submit = wtforms.SubmitField(
        label="提交",
        render_kw={
            "class": "btn btn-primary btn-block",
        },
    )