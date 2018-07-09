#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Flynn on 2018-07-09 22:39


from wtforms import Form, FileField, StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed


class UploadFileForm(Form):
	avatar = FileField(validators=[
		FileRequired(),  # 文件必须上传
		FileAllowed(['jpg', 'png', 'gif'])  # 设置可上传文件格式
	])
	desc = StringField(validators=[
		InputRequired()
	])
