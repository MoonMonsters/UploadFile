import os

from flask import Flask, request, render_template, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename

from forms.upload_file_form import UploadFileForm
from werkzeug.datastructures import CombinedMultiDict

app = Flask(__name__)

UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'upload/image')


@app.route('/upload/', methods=['POST', 'GET'])
def settings():
	if request.method == 'GET':
		return render_template('main.html')
	else:
		form = UploadFileForm(CombinedMultiDict([request.form, request.files]))
		if form.validate():
			desc = request.form.get('desc')
			avatar = request.files.get('avatar')
			filename = secure_filename(avatar.filename)
			avatar.save(os.path.join(UPLOAD_PATH, filename))
			print(desc)
			return '文件上传成功'
		else:
			print(form.errors)
			return '文件上传失败'


@app.route('/image/<filename>/', methods=['GET', 'POST'])
def get_image(filename):
	return send_from_directory(UPLOAD_PATH, filename)


if __name__ == '__main__':
	app.run()
